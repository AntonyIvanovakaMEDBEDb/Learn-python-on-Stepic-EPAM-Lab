a = int(input('Put the  A here '))
b = int(input('Put the  B here '))
# сравним
if b < a:
    print('B is beated')
else:
    print('Ok B is won')
    for x in range(b):
        if x == a:
            print(x, "Look! This was A")
        else:
            print(x)



