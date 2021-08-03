for i in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    m = max(l)
    l = min(l)
    if m - l > x:
        print("NO")
    else:
        print("YES")
