t = int(input())
for i in range(0, t):
    s = input().split(" ")
    k = int(s[1])
    a = input().split(" ")
    l = list(map(int, a))
    m = k // 10
    n = k // 2
    c = 0
    p = 0
    for i in range(0, len(l)):
        if(int(l[i]) >= n):
            c = c + 1
        if(int(l[i] <= m)):
            p = p + 1
    if(p == 2 and c == 1):
        print("yes")
    else:
        print("no")
