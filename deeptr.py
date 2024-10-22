from lib.module2 import *


def main():
    text = "Привіт, як справи?"
    src_lang = "uk"
    dest_lang = "en"

    translated_text = Translate(text, src_lang, dest_lang)
    print(f"Translated Text: {translated_text}")

    lang_detected = LangDetect(text)
    print(f"Detected Language and Confidence: {lang_detected}")

    lang_code = CodeLang("English")
    print(f"Language Code for 'English': {lang_code}")

    print("\nLanguage List Example:")
    LanguageList("screen", text)


if __name__ == "__main__":
    main()
