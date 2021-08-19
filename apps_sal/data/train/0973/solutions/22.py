t = int(input())
for i in range(0, t):
    (n, k) = list(map(int, input().split()))
    x = list(map(int, input().split()))
    a = max(x) + k
    b = min(x) - k
    print(a - b)
