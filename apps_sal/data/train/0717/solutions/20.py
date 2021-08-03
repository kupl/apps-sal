t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    pos = y * 2
    pos1 = (x - 1) * 2
    print(pos + pos1)
