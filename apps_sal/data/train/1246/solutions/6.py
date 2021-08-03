# cook your dish here\
try:

    for _ in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        ln = list(map(int, input().split()))
        a = max(l)
        b = max(ln)
        if a == b:
            print("NO")
        else:
            print("YES")
except:
    pass
