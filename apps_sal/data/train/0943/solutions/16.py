t = int(input())
for _ in range(t):
    (v, w) = map(int, input().split())
    max_p = v + 1
    if w < v:
        max_p = max_p - (v - w)
    print(max_p)
