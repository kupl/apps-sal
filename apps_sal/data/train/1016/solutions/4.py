T = int(input())
for i in range(T):
    N = int(input())
    co = 0
    for j in range(N):
        a, b = map(int, input().split())
        if b - a > 5:
            co += 1
    print(co)
