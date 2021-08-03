t = int(input().strip())
for _ in range(t):
    v, w = tuple(map(int, input().strip().split()))
    print(min(w + 1, v + 1))
