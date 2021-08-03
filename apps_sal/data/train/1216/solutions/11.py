for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #f = False
    if max(a) >= x:
        print("YES")
    else:
        print("NO")
