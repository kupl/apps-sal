t = int(input())
for l in range(t):
    n = int(input())
    t = list(map(int, input().strip().split()))
    for i in t:
        if i % 2 == 0:
            print('NO')
            break
    else:
        print('YES')
