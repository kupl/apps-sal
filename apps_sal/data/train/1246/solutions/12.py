try:
    t1 = int(input())
    for _ in range(t1):
        n = int(input())
        l1 = list(map(int, input().split()))
        l2 = list(map(int, input().split()))
        if max(l1) != max(l2):
            print('YES')
        else:
            print('NO')
except:
    pass
