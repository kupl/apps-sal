T = int(input())
for _ in range(T):
    (r, c) = list(map(int, input().split()))
    (x, y) = list(map(int, input().split()))
    result = max(r - 1 - x, x) + max(c - 1 - y, y)
    print(result)
