t = int(input())
for j in range(t):
    (l, b) = list(map(int, input().split()))
    c = 0
    i = 1
    while l > -1 and b > -1:
        if c == 0:
            l = l - i
            i = i + 1
            c = 1
        else:
            b = b - i
            i = i + 1
            c = 0
    if l < 0:
        print('Bob')
    else:
        print('Limak')
