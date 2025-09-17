from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from services.llm import get_llm

def build_translator_chain(endpoint, api_key, api_version, deployment):
    system = SystemMessagePromptTemplate.from_template(
        "Você é um tradutor profissional. Preserve significado, tom e formatação. Não explique, apenas traduza. Se o texto já estiver no idioma alvo, apenas normalize."
    )
    human = HumanMessagePromptTemplate.from_template(
        "Idioma de origem: {source}\nIdioma de destino: {target}\n---\n{format_block}\n---\nTexto:\n{text}"
    )
    prompt = ChatPromptTemplate.from_messages([system, human])
    def formatter(inputs):
        return {"format_block": "Saída apenas com o texto traduzido."}
    parser = StrOutputParser()
    llm = get_llm(endpoint, api_key, api_version, deployment)
    chain = (RunnablePassthrough.assign(format_block=formatter) | prompt | llm | parser).with_config(run_name="translator")
    def invoke(payload):
        result = chain.invoke(payload)
        return {"translation": result}
    return type("TranslatorChain", (), {"invoke": invoke})
