# Tradutor • Azure OpenAI + LangChain

Aplicativo em **Streamlit** que traduz textos usando **Azure OpenAI** através da biblioteca **LangChain**.

## Funcionalidades
- Tradução de texto entre múltiplos idiomas
- Detecção automática de idioma (opcional)
- Seleção manual de idioma de destino
- Interface simples em Streamlit

## Pré-requisitos
- Python 3.9+
- Recurso do [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- Variáveis de ambiente configuradas:
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_API_VERSION`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT`

## Instalação
```bash
pip install -r requirements.txt
```

## Execução
```bash
export AZURE_OPENAI_ENDPOINT=\"https://<seu-endpoint>.openai.azure.com/\"
export AZURE_OPENAI_API_KEY=\"<sua-chave>\"
export AZURE_OPENAI_API_VERSION=\"2024-08-01-preview\"
export AZURE_OPENAI_CHAT_DEPLOYMENT=\"<deployment-do-modelo>\"
streamlit run app.py
```

## Estrutura do Projeto
```
.
├── app.py
├── services/
│   ├── detect.py
│   ├── llm.py
│   ├── translate.py
│   └── utils.py
└── requirements.txt
```

## Observações
- A tradução é realizada pelo modelo definido no deployment do Azure OpenAI.
- A aplicação não armazena textos traduzidos; tudo é processado em tempo real."
