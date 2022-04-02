#найти наибольшее  общее кратное простым перебором
a = int(input())
b = int(input())
if a < b:
    i = a
else:
    i = b
while (i % a != 0) or (i % b != 0):
    i+=1
print(i)
