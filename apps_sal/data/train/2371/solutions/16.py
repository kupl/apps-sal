def solve(n, a):
    increasing = True
    prev = float('-inf')
    for i in range(n-1, -1, -1):
        if a[i] < prev and increasing:
            increasing = False
        if a[i] > prev and not increasing:
            return i+1
        prev = a[i]
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # x, y, z = map(int, input().split())
    print(solve(n, a))
