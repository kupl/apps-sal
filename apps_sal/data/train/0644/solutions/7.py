for i in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    s = sum(m)
    if s % n == 0:
        print('Yes')
    else:
        print('No')
