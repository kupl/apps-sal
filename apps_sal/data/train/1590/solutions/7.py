for t in range(int(input())):
    g = list(map(int, input().split()))
    m = max(g)
    g.remove(m)
    m1 = max(g)
    m2 = min(g)
    if(m1 + m2 >= m - 1):
        print("Yes")
    elif(m1 == m2 and m2 == m):
        print("Yes")
    else:
        print("No")
