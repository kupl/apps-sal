t = int(input())
for _ in range(t):
    v, w = list(map(int, input().split()))
    print(min(v, w) + 1)
