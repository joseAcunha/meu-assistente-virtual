from langchain.prompts import PromptTemplate

# Prompt para a busca de produtos
PROMPT_BUSCA_PRODUTOS = PromptTemplate(
    input_variables=["query", "produtos"],
    template="""Você é um assistente de vendas de e-commerce. Sua tarefa é ajudar os clientes a encontrar produtos.
Baseado na consulta do cliente e nos produtos disponíveis, liste os produtos que melhor se encaixam.
Considere as especificações e o preço.

Contexto dos produtos:
{produtos}

Consulta do cliente: "{query}"

Formato da resposta:
Lista de produtos relevantes com nome, preço, categoria e uma breve descrição.
Se não encontrar produtos, diga que não encontrou, mas sugira que o cliente reformule a busca.
"""
)

PROMPT_POLITICAS_LOJA = PromptTemplate(
    input_variables=["query", "politicas"],
    template="""Você é um assistente de e-commerce focado em responder dúvidas sobre as políticas da loja.
Use o contexto fornecido sobre as políticas da loja para responder à pergunta do cliente de forma clara e concisa.
Se a informação não estiver no contexto, diga que não possui a informação e sugira que o cliente entre em contato com o suporte humano.

Contexto das políticas da loja:
{politicas}

Pergunta do cliente: "{query}"

Resposta:
"""
)

PROMPT_CONSULTA_PEDIDOS = PromptTemplate(
    input_variables=["query", "pedido_info"],
    template="""Você é um assistente de e-commerce focado em fornecer informações sobre pedidos.
Baseado nas informações do pedido fornecidas, responda à pergunta do cliente.
Se o número do pedido não for encontrado ou a informação solicitada não estiver disponível, informe isso ao cliente.

Informações do pedido:
{pedido_info}

Pergunta do cliente: "{query}"

Resposta:
"""
)

PROMPT_RECOMENDACAO = PromptTemplate(
    input_variables=["query", "produtos_sugeridos"],
    template="""Você é um assistente de e-commerce que faz recomendações de produtos.
Baseado na preferência do cliente e nos produtos que podem ser relevantes, sugira produtos do seu catálogo.

Contexto dos produtos para sugestão:
{produtos_sugeridos}

Preferência do cliente: "{query}"

Sugestões de produtos:
"""
)

PROMPT_DECISAO_ACAO = PromptTemplate(
    input_variables=["question"],
    template="""Analise a seguinte pergunta do cliente e determine a intenção principal.
Responda com uma das seguintes categorias: "busca_produto", "politica_loja", "consulta_pedido", "recomendacao", "saudacao_geral".
Se a pergunta não se encaixar claramente em nenhuma dessas categorias, use "saudacao_geral".

Exemplos:
- "Quero um notebook": busca_produto
- "Como troco um item?": politica_loja
- "Qual o status do meu pedido #123?": consulta_pedido
- "Me sugira algo para presentear meu pai": recomendacao
- "Oi, tudo bem?": saudacao_geral

Pergunta do cliente: "{question}"
Intenção:
"""
)