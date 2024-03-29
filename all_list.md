```
pip install regex
```
0. Подготовка
В этом листке нам не понадобится никаких новых библиотек! Ура!

Вместо этого мы научимся работать со строками в Python.

Полезные ссылки:

Строки в Python (официальная документация)
Python string best practices
String concatenation [https://stackoverflow.com/questions/39675898/is-python-string-concatenation-bad-practice]
String formatting [https://realpython.com/python-string-formatting/]
Обратите внимание: в этом листке сохраняются уровни заданий, как в предыдущем. Вы сами можете решить, сколько заданий вы делаете. На 5 нужно сделать все задания 1, 2 и 3 уровня, на 4 все задания 1 и 2 уровня, на 3 все задания 1 уровня.

Пожалуйста, прочтите все задачи перед тем, как начинать их решать.

1. Извлечение данных из текста
Задача 1. Поиск текста
Скачайте текст любой художественной книги (руками, но можно и программно) в формате txt. Нам потребуется такая книга, в которой хотя бы 10 разных персонажей (но лучше не больше 50). Лучше выбрать текст на английском языке, а не на русском (потому что там нет склонений), но можно и на русском. Положите его в папку с ноутбуком, если вы делаете задание в Jupyter Notebook, или загрузите на Colab. Выведите в ячейке ниже первые 100 символов текста книги.

Замечание: легально и бесплатно можно скачать книги на Project Gutenberg. Например, можно выбрать книгу из наиболее загружаемых.
```
f = open("The War of the Worlds.txt","r")
text = f.read(100)
print(sentence)
```
Дальше мы хотим решить такую задачу: построить по тексту книги граф общения между персонажами. В простейшем случае нас интересует то, что персонажи упоминаются в одном предложении.

Задача 2. Разбиение текста на предложения
Разбейте текст книги на предложения. А именно, напишите функцию, которая принимает на вход одну строку, а возвращает массив строк, где каждая строка -- это предложение исходного текста. Концом предложения считается точка, вопросительный и восклицательный знаки.
```
import re
f = open("The War of the Worlds.txt","r")
text = f.read()
sentence = re.split("[.?!]",text)
print(sentence)
```
Простейшее, с чего мы начнём -- это счётчик того, сколько раз персонажи встретились в одном предложении. Персонажей из текста можно извлекать по-разному, в том числе и сложными методами.

Задача 3. Извлечение персонажений
Уровень 1. У персонажей обычно есть имена. Их могут называть по-разному, но мы будем считать, что одно имя -- это один персонаж. Напишите функцию, которая проходит по всем предложениям и выводит список слов, которые написаны с заглавной буквы, но встретились не в начале предложения. Функция должна возвращать список таких слов. После этого вручную выберите из этого списка те слова, которые действительно являются именами персонажей.

Уровень 2. Придумайте любое улучшение этой простой стратегии, которое позволит точнее извлекать персонажей и меньше делать руками. Реализуйте его.
```import re

f = open("The War of the Worlds.txt","r")
text = f.read()
text = text.replace('\n','')
text = text.replace('`','')
text = text.replace('(','')
text = text.replace('"','')
words = re.split("\s|[,.]",text)
sentences = re.split("[.!?]", text)
words = [word for word in words if word != '']

first_words = [sent.split() for sent in sentences if(sent != '') and (sent != ' ')]
other_words = [sent.split()[1:-1] for sent in sentences if(sent != '')]
other_words = sum(other_words,[])
names = [word for word in other_words if word.istitle()]
names = list(set(names))
verbs = ['has', 'got','said','is', 'was', 'does', 'wanted', 'did']
not_names = [ 'He',  'What', 'This', 'Where', 'Which','That', 'I', 'You', 'It', 'How', 'Why', 'When', 'But', 'Nature', 'Deputation', 'Thing', 'Death','Mars', 'London', 'Monday', 'Asia', 'June', 'Londoners', 'Lord','Hill','Friday','Who', 'She', 'Somebody', 'Here', 'There','England', 'Square', 'Street']#сюда - наречия
true_names = []
for i in range(0,len(words) - 1):
  if words[i] in names and words[i + 1] in verbs and words[i] not in not_names:
    true_names.append(words[i])
true_names = list(set(true_names))
print(true_names)
```

Задача 4. Персонажи из одного предложения
Уровень 1. Используя получившийся список персонажей, снова пройдите по предложениям и посчитайте, сколько раз каждая пара персонажей упоминалась в одном предложении. Для подсчёта можно использовать словарь или двумерный массив.

Уровень 3. Придумайте более сложный механизм подсчёта. Несколько идей: а что персонажи друг другу говорят? Как оно окрашено? Необязательно применять готовые анализаторы -- можно придумать эвристику на основе анализа "плохих" и "хороших" слов.
```
import re
f = open("The War of the Worlds.txt","r")
text = f.read()
text = text.replace('\n','')
text = text.replace('`','')
text = text.replace('(','')
text = text.replace('"','')
words = re.split("\s|[,.]",text)
sentences = re.split("[.!?]", text)
words = [word for word in words if word != '']

first_words = [sent.split() for sent in sentences if(sent != '') and (sent != ' ')]
other_words = [sent.split()[1:-1] for sent in sentences if(sent != '')]
other_words = sum(other_words,[])
names = [word for word in other_words if word.istitle()]
names = list(set(names))
verbs = ['has', 'got','said','is', 'was', 'does', 'wanted', 'did']
not_names = [ 'He',  'What', 'This', 'Where', 'Which','That', 'I', 'You', 'It', 'How', 'Why', 'When', 'But', 'Nature','No', 'Deputation', 'Thing', 'Death','Mars', 'London', 'Monday', 'Asia', 'June', 'Londoners', 'Lord','Hill','Friday','Who', 'She', 'Somebody', 'Here', 'There','England', 'Square', 'Street']#сюда - наречия
true_names = []
for i in range(0,len(words) - 1):
  if words[i] in names and words[i + 1] in verbs and words[i] not in not_names:
    true_names.append(words[i])
true_names = list(set(true_names))
pair_count = dict()

for true_name in true_names:
     pair_count[true_name] = dict()

for sentence in sentences:
     true_names_in_sentence = {true_name for true_name in true_names if true_name in sentence}
     for word in true_names_in_sentence:
          other_words = true_names_in_sentence - {word}
          for oword in other_words:
               pair_count[word][oword] = pair_count[word].get(oword, 0) + 1
               pair_count[oword][word] = pair_count[oword].get(word, 0) + 1
for name in pair_count:
  for oname in pair_count[name]:
    print(name, " and ",oname,' ',pair_count[name][oname])
```
Задача 5. Граф общения
С помощью networkx реализуйте отрисовку графа общения персонажей на основе тех счётчиков, которые вы посчитали в предыдущей задаче.

Уровень 1. Изобразите граф, где вершины относятся к людям, а рёбра -- к факту того, что счётчик этой пары людей превысил, например, 5 (то есть в одном предложении эти люди встречались 5 раз). Можно попробовать разные числа вместо 5 и посмотреть, что получится.

Уровень 2. Подпишите вершины графа.

Уровень 3. Цвет (и, возможно, толщина) рёбер графа должна соответствовать тому, сколько эти персонажи общаются в книге
```
Ничего личного , сори , но я это задание не сделал .
```
