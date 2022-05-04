"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""
from typing import List
arr_a: List[List[str]] = []
arr_b = []
i = 0
j = 0
elem = 0
n = 0
m = 0
line_i = input().split()
while 'end' not in line_i:  # заполняем матрицу  строками пока  не  получим  на входе  'end'
    n = len(line_i)
    for i in range(len(line_i)):
        line_i[i] = int(line_i[i])
    arr_a.append(line_i)
    line_i = input().split()
    m += 1

# print(arr_a)
# print(arr_a[-1][-1])
# формируем  результирующую  матрицу  по  условиям  задачи
i = 0
j = 0
for i in range(len(arr_a)):
    if i == m:
        i = -1
    for j in range(len(arr_a[i])):
        if j == n:
            j = -1
        print(arr_a[i - 1][j], end=' ')
        print(arr_a[i + 1][j], end=' ')
        print(arr_a[i][j - 1], end=' ')
        print(arr_a[i][j + 1], end=' ')
        pass
        """
        elem = arr_a[i-1][j] + arr_a[i+1][j] + arr_a[i][j-1] + arr_a[i][j+1]
        arr_b[i][j] = int(elem)
        pass
        print(arr_b[i][j], end = ' ')
        """
    print()                     # делаем переход на новую строку


    # print(line_i)
    # lst = [int(i) for i in input().split()]
