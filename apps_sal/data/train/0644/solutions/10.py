t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 0:
        print('No')
    else:
        x = sum(a) // n
        if x * n == sum(a):
            print('Yes')
        else:
            print('No')
