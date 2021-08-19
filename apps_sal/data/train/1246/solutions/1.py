try:
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        (ma, mb) = (max(a), max(b))
        if abs(ma - mb):
            print('YES')
        else:
            print('NO')
except:
    pass
