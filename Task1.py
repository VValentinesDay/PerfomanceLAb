
n = int(input("Введите число n "))
m = int(input("Введите число длины обхода m ")) - 1
if n < m:
    print("n не может быть меньше m")
    while n < m:
        m = int(input("Введите число длины обхода m "))
a = ''
for i in range(1, n + 1):
    a += str(i)
# print('Изначальный массив', a)
end = -1

open = a[0]
start = 0
space = ''
end_1 = m

t = 0

while open != end:
    space += a[start]
    end = a[end_1]
    a += a
    # print(a[start], ' - начало,', a[end_1],  ' - конец', '|', start, ' - start,', m, ' - m')
    start += m
    end_1 = start + m
# print(f"Полученный путь = {space}")
print(space)
