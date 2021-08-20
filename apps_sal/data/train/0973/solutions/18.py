t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    z = list(map(int, input().split()))
    a = min(z) - k
    b = max(z) + k
    print(abs(b - a))
