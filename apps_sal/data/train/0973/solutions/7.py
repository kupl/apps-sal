t = int(input())
while t > 0:
    t -= 1
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()[:n]))
    mx = max(a) + k
    mn = min(a) - k
    print(mx - mn)
