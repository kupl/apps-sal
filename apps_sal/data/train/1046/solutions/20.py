t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    m = 1
    n = 2
    while(1):
        if(a < m):
            print('Bob')
            break
        elif(b < n):
            print('Limak')
            break
        a = a - m
        b = b - n
        m = m + 2
        n = n + 2
