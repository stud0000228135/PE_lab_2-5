# Установка необходимых библиотек
!pip install streamlit transformers sentencepiece

# Импорт библиотек
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Загрузка модели для анализа тональности
sentiment_classifier = pipeline("sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")

# Загрузка модели для машинного перевода
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")

# Загрузка токенизатора для машинного перевода
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")

# Функция для анализа тональности
def analyze_sentiment(text):
    result = sentiment_classifier(text)
    return result[0]['label']

# Функция для машинного перевода
def translate_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

# Стартовая страница Streamlit
st.title("Машинное обучение и NLP с Streamlit")

# Элемент управления для ввода текста
user_text = st.text_area("Введите текст:")

# Элемент управления для анализа тональности
if st.button("Анализ тональности"):
    sentiment_result = analyze_sentiment(user_text)
    st.write(f"Результат анализа тональности: {sentiment_result}")

# Элемент управления для машинного перевода
if st.button("Перевести текст"):
    translation_result = translate_text(user_text)
    st.write(f"Результат перевода: {translation_result}")
