from langchain_openai import AzureChatOpenAI

def get_llm(endpoint, api_key, api_version, deployment, temperature=0.2):
    return AzureChatOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
        azure_deployment=deployment,
        temperature=temperature,
        max_tokens=1024,
        streaming=False,
    )
