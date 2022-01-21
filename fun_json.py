import random
import json  # идеально подходит для хранения данных типа словарь
from sklearn.feature_extraction.text import CountVectorizer  # библиотека векторайзеров,
# библиотека классификаторов
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# открываем файл со всеми интентами и ответами
with open('Intents.json', 'r', encoding="utf-8") as f:
    BOT_CONFIG = json.load(f)  # вызываем функцию для файла, в котором будут все наши интенты
    len(BOT_CONFIG['intents'].keys())
    #  print(len(BOT_CONFIG['intents'].keys()))


def clean(text):  # чистим текст, делаем бота умнее
    clean_text = ''
    for simbol in text.lower():
        if simbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            clean_text = clean_text + simbol
    return clean_text


# Обучаем Бота
texts = []  # нужно получить примеры всех и интентов
y = []   # ответы бота и нужно пары классифицировать
for intent in BOT_CONFIG['intents'].keys():
    for example in BOT_CONFIG['intents'][intent]['examples']:
        texts.append(example)
        y.append(intent)
    len(texts), len(y)


train_texts, test_texts, y_train, y_test = train_test_split(
    texts, y, random_state=42, test_size=0.2)


vectorizer1 = CountVectorizer(ngram_range=(1, 3), analyzer='char_wb')  # объект класса векторайзер
x_train = vectorizer1.fit_transform(train_texts)  # передаем список текста через функцию fit_transform,
x_test = vectorizer1.transform(test_texts)        # вектор соответсвующий тексту
slovar = vectorizer1.get_feature_names_out()  # наш список из всех слов, которые есть в словаре
# len(slovar)

# теперь нужно, чтобы бот умел классифицировать текст
classificator = RandomForestClassifier(n_estimators=300).fit(x_train, y_train)  # создаем классификатор


def get_intent_by_model(text):
    return classificator.predict(vectorizer1.transform([text]))[0]


def bot_json(inpu_text):  # Функция Бота, которая будет отвечать случайным образом из ответов
    intent1 = get_intent_by_model(inpu_text)
    return random.choice(BOT_CONFIG['intents'][intent1]['responses'])


# inpu_text = ''  # запускаем бесконечный цикл
# while inpu_text != 'stop':  # слово стоп прерывает цикл
#     inpu_text = input()
#     if inpu_text != 'stop':
#         response = bot(inpu_text)
#         print('lol',response)









