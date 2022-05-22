''' Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка
'''
def modify_list(l):
    '''
    Функция  к  заданию 3.1.2
    функция  модифицирует  список
    '''
    i = 0
    while i <= int(len(l)-1):
        if (l[i] % 2) != 0:
            l.pop(i)
        else:
            l[i] = l[i] // 2
            i += 1
'''
А теперь ее вызов
'''
lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)
lst = [1]
modify_list(lst)
print(lst)
lst = [2]
modify_list(lst)
print(lst)
lst = []
modify_list(lst)
print(lst)
lst = [8, 1, 0, 3, 4, 5, 6]
modify_list(lst)
print(lst)
lst = [-8, 1, 0, 3, 4, 5, 6, 8, 10, -12, -11]
modify_list(lst)
print(lst)