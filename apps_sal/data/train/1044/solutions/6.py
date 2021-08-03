n = int(input())
suma = []
for i in range(0, n):
    x = input()
    x = list(x)
    a = 0
    for i in x:
        a = a + int(i)
    suma.append(a)
for i in suma:
    print(i)
