for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    x = []
    for i in range(len(b)):
        if b[i] in a:
            x.append(a.index(b[i]))
    c = 0
    g = sorted(x)
    if len(x) > 1:
        if x == g:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
