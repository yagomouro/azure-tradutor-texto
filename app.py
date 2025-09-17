import os
import streamlit as st
from services.detect import detect_language
from services.translate import build_translator_chain
from services.utils import LANGS, normalize_lang_label

st.set_page_config(page_title="Tradutor • Azure OpenAI + LangChain", layout="centered")

st.title("Tradutor • Azure OpenAI + LangChain")

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

if not all([endpoint, api_key, deployment]):
    st.error("Defina AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY e AZURE_OPENAI_CHAT_DEPLOYMENT.")
else:
    txt = st.text_area("Texto de entrada", height=220)
    col1, col2 = st.columns(2)
    with col1:
        auto = st.toggle("Detectar idioma automaticamente", value=True)
    with col2:
        tgt = st.selectbox("Idioma de destino", options=list(LANGS.keys()), index=list(LANGS.keys()).index("Português"))
    run = st.button("Traduzir")
    if run and txt.strip():
        src = detect_language(txt) if auto else None
        chain = build_translator_chain(endpoint, api_key, api_version, deployment)
        with st.spinner("Traduzindo..."):
            out = chain.invoke({"text": txt, "target": normalize_lang_label(tgt), "source": src})
        st.subheader("Resultado")
        st.markdown(out["translation"])
        with st.expander("Metadados"):
            st.json({"detected_source": src, "target": tgt, "model_deployment": deployment})
