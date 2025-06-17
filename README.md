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

## ⚙️ Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

* **Python 3.9+** (Recomendado Python 3.10 ou superior)
* **Git Bash** (No Windows, para melhor experiência com comandos de terminal)
* **Chave da API OpenAI:** Você precisará de uma chave de API para o OpenAI. Obtenha uma em [platform.openai.com](https://platform.openai.com/).

### 1. Clonar o Repositório

```bash
git clone [https://github.com/joseAcunha/meu-assistente-virtual.git](https://github.com/joseAcunha/meu-assistente-virtual.git)
cd meu-assistente-virtual