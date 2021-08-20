try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        if max(a) != max(b):
            print('YES')
        else:
            print('NO')
except EOFError as e:
    pass
