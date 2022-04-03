# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.
# get the  numbers using  list & split  method
# a, b = (int(i) for i in input().split())
# if we need to get numbers  step by step
a = int(input())
b = int(input())
s_av = 0 #here  we  will caculate  the  average  of  list
count_of_3multiple = 0 #here  we  will accumulate  the  count  of items multiple of 3
for i in range(a,(b + 1)):
    if i % 3 == 0:
        s_av += i
        count_of_3multiple += 1
# print  the  average of  numbers  which are  multiple of 3
print(s_av/count_of_3multiple)


