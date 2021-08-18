for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    m = max(l)
    n = min(l)
    if(m - n < k):
        print("YES")
    else:
        print("NO")
