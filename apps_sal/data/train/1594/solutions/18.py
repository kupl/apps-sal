t = int(input())
for i in range(t):
    n = int(input())
    swa = 0
    suma = 0
    for j in range(0, n):
        s = input()
        for k in range(0, n):
            if s[k] == '1':
                swa = swa + abs(k - j)
    while n >= 1:
        suma += n
        n = n - 1
    if swa == 0:
        print(suma)
    else:
        print(suma - swa + 1)
