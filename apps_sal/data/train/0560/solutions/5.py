T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = max(a)
    y = max(b)
    a.remove(x)
    b.remove(y)
    suma = 0
    sumb = 0
    for i in a:
        suma = suma + i
    for i in b:
        sumb = sumb + i
    if suma < sumb:
        print('Alice')
    elif suma > sumb:
        print('Bob')
    else:
        print('Draw')
