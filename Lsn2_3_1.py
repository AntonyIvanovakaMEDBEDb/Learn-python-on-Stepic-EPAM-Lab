# Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b] на все
# числа отрезка [c;d].
#  Числа a, b, c и d являются натуральными и не превосходят 10, a ≤ b, c ≤ d.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('   \t', end='')
for j in range(c,(d + 1) ):
    print(j, '\t', end='')
print()
for i in range(a, (b + 1)):
    print (i, end='')
    for j in range(c,(d + 1) ):
        print('\t', (i * j), end='')
    print()
