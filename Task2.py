'''
Task2

Напишите программу, которая рассчитывает положение точки относительно окружности
Соответствия ответов:
0 - точка лежит на окружности
1 - точка внутри
2 - точка снаружи
'''

import sys

a = sys.argv[1]
b = sys.argv[2]

file1 = open(a, "r")
file2 = open(b, "r")





def compare(x0, y0, r, x, y):
    '''
    Определение положения точки относительно окружности. Для этого определяется расстояние между точкой и центром окружности,
    :param x0: Координата центра окружности
    :param y0: Координата центра окружности
    :param r: Радиус
    :param x: Координата точки
    :param y: Координата точки
    :return: Соответсвующие ответы
    '''
    d = ((x - x0) ** 2 + (y - y0) ** 2)**(1/2)
    if x0 - r <= x <= x0 + r and y0 - r <= y <= y0 + r:
        if d < r:
            # print('Точка внутри окружности\n')
            return 1
        elif d == r:
            # print('Точка на окружности\n')
            return 0
        else:
            # print('Точка за окружностью\n')
            return 2
    else:
        # print('Точка за окружностью\n')
        return 2


def read_and_compare(file1, file2):
    '''
    Считываются два файла, после чего данные проверяются согласно условию задачи.
    :param file1: Файл с параметрами окружности
    :param file2: Файл с координатами точек
    :return: - Функция лишь печатает запрашиваемые данные
    '''
    l = []
    while True:
        line = file1.readline()
        if not line:
            break
        l.extend(line.strip().split())
    l = [int(i) for i in l]
    x0 = l[0]
    y0 = l[1]
    r = l[2]
    # print(l)

    # Считывание файла 2
    xy = []
    c = 0
    while True:
        line = file2.readline()
        # Прерывается цикл, если строка пустая. Предполагается, что координаты разделены, не более чем 2-мя пустыми строками.
        if not line:
            c += 1
            if c == 3:
                break
        xy.extend(line.strip().split())
        if len(xy) == 2:
            xy = [int(i) for i in xy]
            x = xy[0]
            y = xy[1]

            print(compare(x0, y0, r, x, y), end = '\n')

        xy.clear()

read_and_compare(file1, file2)