'''
Выведите таблицу размером n×n, заполненную числами от 1 до n*n
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5):
'''
n = int(input())
i = 0
# We should  make  an  empty matrix NxN
a = [None] * n
for i in range(n): a[i] = [None] * n
x: int
y: int
i: int
x, y = 0, 0
# y = 0
# dx , dy  - are increments
dx = 1
dy = 0
i = 0
for i in range(n * n):
    a[y][x] = i + 1  # Here we are setting next item of matrix
    # Here we calculate the  test  value  which help as  to prevent go out  of  range
    test = x + dx if dx else y + dy
    # cheking for the  out of  range  condition and not  empy cell
    if test < 0 or test == n or a[y + dy][x + dx] is not None:
        dx, dy = -dy, dx
    x += dx
    y += dy
# Print result  without  commas and square brackets
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x], end = ' ')
    print()
