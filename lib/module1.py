from googletrans import Translator, LANGUAGES

translator = Translator()


def Translate(text: str, scr: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error during translation: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        result = translator.detect(text)
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return f"{result.confidence:.2f}"
        return f"Detected(lang={result.lang}, confidence={result.confidence:.2f})"
    except Exception as e:
        return f"Error during language detection: {str(e)}"


def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code
    return "Language or code not found."


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        languages = [
            (i + 1, name.capitalize(), code)
            for i, (code, name) in enumerate(LANGUAGES.items())
        ]

        header = (
            f"{'N':<3} {'Language':<20} {'ISO-639 code':<10} {'Text':<30}\n{'-'*70}"
        )
        rows = []

        for num, lang, code in languages:
            translated_text = Translate(text, "auto", code) if text else ""
            rows.append(f"{num:<3} {lang:<20} {code:<10} {translated_text:<30}")

        output = header + "\n" + "\n".join(rows)

        if out == "screen":
            print(output)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(output)

        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
