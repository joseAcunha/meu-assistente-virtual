# 🛍️ Assistente Virtual de E-commerce

Um assistente virtual inteligente desenvolvido com FastAPI e LangChain, projetado para auxiliar clientes em um e-commerce com informações sobre produtos, políticas da loja, status de pedidos e recomendações personalizadas.

---

## ✨ Funcionalidades

* **Busca de Produtos:** Responde a perguntas sobre produtos específicos, características e ajuda a encontrar o item ideal.
* **Informações sobre Políticas:** Fornece detalhes sobre políticas da loja (trocas, devoluções, prazos de entrega, garantia, pagamentos).
* **Consulta de Pedidos:** Permite verificar o status e detalhes de um pedido usando seu ID.
* **Recomendações Personalizadas:** Sugere produtos com base nas preferências ou interesses gerais do cliente.
* **Interface de Chat Amigável:** Frontend web simples e intuitivo para interação direta com o assistente.
* **Roteamento Inteligente:** Utiliza ferramentas (LangChain Agents) para direcionar a consulta do usuário à funcionalidade correta.

---

## 🚀 Tecnologias Utilizadas

**Backend (API):**
* **Python:** Linguagem de programação principal.
* **FastAPI:** Framework web moderno e rápido para construir APIs.
* **LangChain:** Framework para desenvolvimento de aplicações com Large Language Models (LLMs).
    * `langchain-openai`: Conexão com modelos OpenAI.
    * `langchain-community`: Componentes de comunidade.
    * `langchain-core`: Componentes centrais.
    * `langchain-agents`: Para roteamento inteligente e uso de ferramentas.
* **FAISS:** Biblioteca para busca de similaridade eficiente, usada para vetores de produtos e políticas (RAG).
* **Pydantic:** Para validação de dados e modelagem de requisições/respostas da API.
* **Uvicorn:** Servidor ASGI de alta performance para o FastAPI.
* **`python-dotenv`:** Para gerenciar variáveis de ambiente.

**Frontend (Interface Web):**
* **HTML5:** Estrutura da página.
* **CSS3:** estilização rápida e responsiva.
* **JavaScript (ES6+):** Lógica interativa do chat, comunicação com a API.
* **`marked.js`:** Biblioteca para renderização de Markdown no frontend.

---

## ⚙️ Como rodar o projeto (Passo a Passo)

### Pré-requisitos

- **Python 3.9+** (Recomendado Python 3.10 ou superior)
- **Chave da API OpenAI** (obtenha em https://platform.openai.com/)

### 1. Clone o repositório

```bash
git clone https://github.com/joseAcunha/meu-assistente-virtual.git
cd meu-assistente-virtual
```

### 2. Crie e ative um ambiente virtual (recomendado)

No Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\activate
```
No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r deploy/requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (ou dentro da pasta `src/`), com o seguinte conteúdo:

```
OPENAI_API_KEY=sua_chave_openai_aqui
```

### 5. Rode o backend (API FastAPI)

```bash
uvicorn src.api:app --reload
```
Acesse http://127.0.0.1:8000/docs para ver a documentação interativa da API.

### 6. Rode o frontend (interface web)

Basta abrir o arquivo `frontend/index.html` no seu navegador.

> **Dica:** O frontend já está configurado para se comunicar com o backend em `http://127.0.0.1:8000`.

---

## 🛠️ Dicas de uso
- O chat aceita perguntas sobre produtos, políticas, pedidos (use o ID do pedido, ex: #12345) e recomendações.
- Se encontrar algum erro, verifique se a chave da OpenAI está correta e se o backend está rodando.

---

## 📄 Licença
MIT
