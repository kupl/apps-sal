t = int(input())
while(t):
    a, b, c = map(int, input().split())
    k = max(a, b, c)
    p = min(a, b, c)
    l = (a + b + c) - k - p
    if k**2 == p**2 + l**2:
        if k + p > l and k + l > p and l + p > k and k - p < l and k - l < p and l - p < k:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t = t - 1
