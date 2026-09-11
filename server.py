"""
Модуль реалізує веб-сервер на базі Flask для виявлення емоцій.
Надає маршрути для відображення головної сторінки та обробки
запитів на аналіз тексту через пакет EmotionDetection.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Обробляє маршрут головної сторінки та рендерить шаблон index.html.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Отримує текст із запиту, передає його у функцію emotion_detector,
    обробляє можливі помилки (порожній ввід) та повертає форматований
    результат з оцінками емоцій.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Недійсний текст! Спробуйте ще раз!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return (
        f"Для даного висловлення відповідь системи: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} та 'sadness': {sadness}. "
        f"Домінуюча емоція - {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
