from langchain.agents import AgentExecutor
from agente import AgenteOpenAIFunctions
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

pergunta = "Quais os dados da Ana?"
pergunta = "Quais os dados da Bianca?"
pergunta = "Quais os dados de Ana e de Bianca?"
pergunta = "Crie um perfil acadêmico para a Ana!"
pergunta = "Compare o perfil academico da Ana com o da Bianca!"
pergunta = "Tenho sentido Ana desanimada com cursos de matematica. Seria uma boa parear ela com a Bianca?"
pergunta = "Quais os dados da USP?"

agente = AgenteOpenAIFunctions()
executor = AgentExecutor(agent=agente.agente,
                       tools=agente.tools,
                       verbose=True)
resposta = executor.invoke({"input": pergunta})
print(resposta)