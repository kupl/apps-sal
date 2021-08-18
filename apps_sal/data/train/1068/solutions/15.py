t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    if((a * b) % 2 == 0):
        print('YES')
    else:
        print('NO')
