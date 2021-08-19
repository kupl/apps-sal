t = eval(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    if n * m == 2:
        print('Yes')
    elif n * m % 2 == 0 and m != 1 and (n != 1):
        print('Yes')
    else:
        print('No')
