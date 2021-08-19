# cook your dish here
try:
    n = int(input())
    for i in range(n):
        c, x = input().split()
        l = list(map(int, input().split()))
        l_min, l_max = min(l), max(l)
        if l_max - l_min > int(x):
            print('NO')
        else:
            print('YES')
except:
    pass
