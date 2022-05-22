def f(x):
    '''
    Функция  к  заданию 3.1.1

    '''
    y = 0
    if x <= -2:
        y = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        y = x / -2
    elif 2 < x:
        y = (x - 2) ** 2 + 1
    return y
'''
А теперь ее вызов
'''
print(f(int(input())))
