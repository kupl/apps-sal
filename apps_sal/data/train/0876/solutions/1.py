for i in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if max(a) - min(a) > x:
        print("NO")
    else:
        print("YES")

