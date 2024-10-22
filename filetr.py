import os
import re
from lib.module1 import *


def read_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")

    config = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key] = value.strip()

    config["max_chars"] = int(config.get("max_chars", 600))
    config["max_words"] = int(config.get("max_words", 100))
    config["max_sentences"] = int(config.get("max_sentences", 10))

    return config


def read_text_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Text file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def count_sentences(text):
    return len(re.split(r"[.!?]+", text)) - 1


def process_text(text, max_chars, max_words, max_sentences):
    sentences = re.split(r"[.!?]+", text)
    words = text.split(" ")

    char_count = 0
    word_count = 0
    sentence_count = 0

    result_text = ""

    for sentence in sentences:
        sentence_words = sentence.split(" ")

        if char_count + len(sentence) > max_chars:
            break

        if word_count + len(sentence_words) > max_words:
            break

        result_text += sentence + " "

        char_count += len(sentence)
        word_count += len(sentence_words)
        sentence_count += 1

    return result_text


def main():
    config_path = "config.txt"

    try:
        config = read_config(config_path)
        text_file = config["text_file"]
        target_language = config["target_language"]
        output_mode = config["output"]
        max_chars = config["max_chars"]
        max_words = config["max_words"]
        max_sentences = config["max_sentences"]

        input_text = read_text_file(text_file)
        print(f"File: {text_file}")
        print(f"File Size: {len(input_text)} characters")
        print(f"Word Count: {len(input_text.split())}")
        print(f"Sentence Count: {count_sentences(input_text)}")

        processed_text = process_text(input_text, max_chars, max_words, max_sentences)
        print(f"Processed Text: {processed_text[:100]}...")

        detected_language = LangDetect(processed_text, "lang")
        print(f"Detected Language: {detected_language}")

        translated_text = Translate(processed_text, detected_language, target_language)

        if output_mode == "screen":
            print(f"\nTranslated Text ({target_language}):")
            print(translated_text)
        elif output_mode == "file":
            output_file = f"output_{target_language}.txt"
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(translated_text)
            print("Ok")
        else:
            print("Invalid output mode in config file.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
