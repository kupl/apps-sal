
T = int(input())

for q in range(T):
    x, y = list(map(int, input().strip().split()))

    y = (y - 1) // x

    print(x * (y) * (y + 1) // 2)
