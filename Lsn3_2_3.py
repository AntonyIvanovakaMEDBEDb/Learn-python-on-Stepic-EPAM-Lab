'''
Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел,
которые нужно считать. Далее считывает n строк с числами Xi , по одному числу в каждой строке.
Итого будет n+1 строк.
При считывании числа Xi программа должна на отдельной строке вывести значение f(Xi).
Функция f(x) уже реализована и доступна для вызова.
Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
'''
def f(x):
    y = 0
    if x <= -2:
        y = 1 - (x + 2)**2
    elif -2 < x <= 2:
        y = x / -2
    elif 2 < x:
        y = (x - 2)**2 + 1
    return y
# reading variable  n. n - number  of strings
n = int(input())
i = 0
out_dct = {}
# make  the  dict  of   function values
for i in  range(n):
    x = float(input())
    if x not in out_dct: # cheking dictionary for existing 'x' if not => adding value  to  dictionary
        out_dct[x] = f(x)
        print(out_dct[x])
    else:
        print(out_dct[x])