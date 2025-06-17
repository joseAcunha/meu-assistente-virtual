import os
import json
import re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import Tool

from src.rag_system import product_vector_store, policy_vector_store, get_relevant_documents, get_recommendation_context

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))

def load_orders_data(file_path="data/pedidos.json"):
    if not os.path.exists(file_path):
        print(f"Erro: Arquivo de pedidos não encontrado em {file_path}")
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

orders_data = load_orders_data()

def get_order_info_tool(order_id: str) -> str:
    for order in orders_data:
        if order['pedido_id'] == order_id:
            return json.dumps(order, ensure_ascii=False, indent=2)
    return "Não foi possível encontrar informações para o pedido com este ID. Por favor, verifique o número e tente novamente."

def parse_order_id_from_query(query: str) -> str | None:
    match = re.search(r'#(\d+)', query)
    if match:
        return match.group(1)
    return None

def get_product_search_results_tool(query: str) -> str:
    relevant_products_context = get_relevant_documents(query, product_vector_store, k=5)
    if relevant_products_context:
        return "Produtos encontrados:\n" + relevant_products_context
    return "Não encontrei produtos que correspondam à sua busca. Tente reformular ou especificar mais."

def get_policy_info_tool(query: str) -> str:
    relevant_policies_context = get_relevant_documents(query, policy_vector_store, k=3)
    if relevant_policies_context:
        return "Informações de política:\n" + relevant_policies_context
    return "Não encontrei informações específicas sobre esta política. Por favor, entre em contato com nosso suporte para mais detalhes."

def get_recommendation_tool(query: str) -> str:
    relevant_products_context = get_recommendation_context(query, product_vector_store, k=5)
    if relevant_products_context:
        return "Sugestões de produtos:\n" + relevant_products_context
    return "Não consegui gerar recomendações claras com base na sua preferência. Posso tentar com uma categoria ou tema diferente?"

tools = [
    Tool(
        name="get_product_search_results",
        func=get_product_search_results_tool,
        description="Útil para buscar produtos com base em descrições, características e preço."
    ),
    Tool(
        name="get_policy_info",
        func=get_policy_info_tool,
        description="Útil para responder perguntas sobre políticas da loja (ex: trocas, devoluções, prazos de entrega, garantia, pagamentos)."
    ),
    Tool(
        name="get_order_info",
        func=get_order_info_tool,
        description="Útil para consultar o status ou detalhes de um pedido específico. O ID do pedido deve ser um número, ex: '12345'."
    ),
    Tool(
        name="get_recommendation",
        func=get_recommendation_tool,
        description="Útil para recomendar produtos com base nas preferências ou interesses gerais do cliente."
    )
]

prompt = ChatPromptTemplate.from_messages([
    ("system", """Você é um assistente virtual de e-commerce amigável e útil.
Sua principal função é auxiliar clientes com busca de produtos, informações sobre políticas da loja, consulta de pedidos e recomendações.
Use as ferramentas disponíveis para buscar as informações necessárias.
Se uma pergunta não se encaixar em nenhuma ferramenta, ou se a ferramenta retornar uma resposta vazia, responda de forma educada e útil, talvez perguntando se pode ajudar com outra coisa.
Sempre tente ser o mais preciso possível e utilize as informações das ferramentas para formular a resposta final.
Quando um ID de pedido for mencionado, tente extraí-lo e passá-lo para a ferramenta `get_order_info`.
"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # verbose=True para ver o raciocínio do agente

def chat_with_assistant(query: str) -> str:
    try:
        response = agent_executor.invoke({"input": query, "chat_history": []})
        return response.get("output", "Desculpe, não consegui processar sua solicitação no momento.")
    except Exception as e:
        print(f"Erro no chat_with_assistant: {e}")
        return "Desculpe, ocorreu um erro inesperado. Por favor, tente novamente mais tarde."

if __name__ == "__main__":
    print("Bem-vindo ao Assistente Virtual de E-commerce! Digite 'sair' para encerrar.")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Até logo!")
            break

        response = chat_with_assistant(user_input)
        print(f"Assistente: {response}")