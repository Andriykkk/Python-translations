from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0


def Translate(text: str, scr: str, dest: str) -> str:
    try:
        if scr == "auto":
            translated = GoogleTranslator(source="auto", target=dest).translate(text)
        else:
            translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Error during translation: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        confidence = "N/A"
        if set == "lang":
            return lang
        elif set == "confidence":
            return confidence
        return f"Detected(lang={lang}, confidence={confidence})"
    except LangDetectException as e:
        return f"Error during language detection: {str(e)}"


def CodeLang(lang: str) -> str:
    languages = GoogleTranslator().get_supported_languages(as_dict=True)
    lang = lang.lower()

    if lang in languages:
        return languages[lang]

    for code, name in languages.items():
        if name.lower() == lang:
            return code
    return "Language or code not found."


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        languages = GoogleTranslator().get_supported_languages(as_dict=True)
        header = (
            f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text':<30}\n{'-'*70}"
        )
        rows = []

        for num, (code, lang) in enumerate(languages.items(), start=1):
            translated_text = Translate(text, "auto", code) if text else ""
            rows.append(
                f"{num:<3} {lang.capitalize():<20} {code:<10} {translated_text:<30}"
            )

        output = header + "\n" + "\n".join(rows)

        if out == "screen":
            print(output)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(output)

        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
