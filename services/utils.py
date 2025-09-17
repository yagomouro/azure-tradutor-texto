LANGS = {
    "Português": "pt",
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Japonês": "ja",
    "Chinês (Simplificado)": "zh",
    "Chinês (Tradicional)": "zh-Hant",
    "Coreano": "ko",
    "Árabe": "ar"
}

def normalize_lang_label(label):
    return LANGS.get(label, label)
