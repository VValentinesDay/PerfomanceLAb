'''
Task3

На вход в качестве аргументов программы поступают два файла: tests.json и values.json (в
приложении к заданию находятся примеры этих файлов)
• values.json содержит результаты прохождения тестов с уникальными id
• tests.json содержит структуру для построения отчёта на основе прошедших тестов
(вложенность может быть большей, чем в примере)

Напишите программу, которая формирует файл report.json с заполненными полями value для
структуры tests.json на основании values.json.'''

import json
import sys

a = sys.argv[1]
b = sys.argv[2]

if a == 'tests.json':
    filename1 = open(a, encoding='utf-8')
    data = json.load(filename1)
    filename2 = open(b, encoding='utf-8')
    data2 = json.load(filename2)
else:
    filename1 = open(b, encoding='utf-8')
    data = json.load(filename1)
    filename2 = open(a, encoding='utf-8')
    data2 = json.load(filename2)



def list_maker(data, list_data = []):
    '''
    Создание промежуточного списка для изятия из него значений. Вероятно, шаг необязательный, сделан по неопытности.
    :param data: values.json. Содержимое указанного файла распаковывается и представляется в виде листа
    :param list_data: Пустой лист для далньнейшего заполнения
    :return: Функция меняет уже существующий объект
    '''
    if type(data) == dict:
        for k, j in data.items():
            if k == 'id' :
                list_data.append([k, j])
            elif k == 'title':
                list_data[-1].extend([k, j])
            elif k == 'value':
                list_data[-1].extend([k, j])
            else:
                list_maker(j)
    elif type(data) == list:
        for i in data:
            list_maker(i)
    return list_data

def unpuck_and_change(data, data2):
    '''
    Изменение файла tests.json с дальнешем изменением полей values и сохранением нового файла.

    :param data: tests.json
    :param data2: Лист, результат выполнения list_maker. Из него беруться значения value.
    :return: Функция меняет уже существующий, изменяемый объект data
    '''
    if type(data) == dict:
        for k, j in data.items():
            if k == 'id':
                key = j
            if k == 'value':
                for i in range(len(data2)):
                    for l in data2[i]:
                        if l == key:
                            data['value'] = data2[i][3]
            else:
                unpuck_and_change(j, data2)
    elif type(data) == list:
        for i in data:
            unpuck_and_change(i, data2)


d2 = list_maker(data2)
datares = unpuck_and_change(data, d2)

#Запись данных
filename = 'report.json'

with open (filename, 'w', encoding = "utf-8") as f:
    json.dump(data, f, ensure_ascii = False, indent= 2)

