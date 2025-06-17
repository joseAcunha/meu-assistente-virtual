import json
import os
import markdown
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

def load_products_data(file_path="data/produtos.json"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_policies_data(file_path="data/politicas.md"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def create_product_documents(products):
    documents = []
    for prod in products:
        content = f"ID: {prod['id']}\nNome: {prod['nome']}\nCategoria: {prod['categoria']}\nPreço: R${prod['preco']:.2f}\nDescrição: {prod['descricao']}\nEspecificações: {json.dumps(prod['especificacoes'], ensure_ascii=False)}"
        documents.append(Document(page_content=content, metadata={"type": "product", "id": prod['id'], "name": prod['nome']}))
    return documents

def create_policy_documents(policies_text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    docs = [Document(page_content=policies_text, metadata={"type": "policy"})]
    return text_splitter.split_documents(docs)

def build_vector_store(documents, db_path="faiss_index"):
    if not os.path.exists(db_path):
        print(f"Criando novo índice FAISS em {db_path}...")
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(db_path)
        print("Índice FAISS criado e salvo.")
    else:
        print(f"Carregando índice FAISS existente de {db_path}...")
        vector_store = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
        print("Índice FAISS carregado.")
    return vector_store

def get_relevant_documents(query: str, vector_store, k=5):
    docs = vector_store.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])

products_data = load_products_data()
policies_text = load_policies_data()

product_docs = create_product_documents(products_data)
policy_docs = create_policy_documents(policies_text)

all_documents = product_docs + policy_docs

product_vector_store = build_vector_store(product_docs, "faiss_product_index")
policy_vector_store = build_vector_store(policy_docs, "faiss_policy_index")

def get_recommendation_context(query: str, vector_store, k=5):
    docs = vector_store.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])

if __name__ == "__main__":
    print("Testando busca de produtos:")
    query_prod = "notebook para programar"
    relevant_products_context = get_relevant_documents(query_prod, product_vector_store, k=3)
    print(f"\nContexto para '{query_prod}':\n{relevant_products_context}")

    print("\nTestando busca de políticas:")
    query_policy = "como trocar um produto"
    relevant_policies_context = get_relevant_documents(query_policy, policy_vector_store, k=2)
    print(f"\nContexto para '{query_policy}':\n{relevant_policies_context}")