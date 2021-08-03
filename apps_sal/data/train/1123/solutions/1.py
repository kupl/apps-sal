t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    l = [0] * n
    for j in range(0, n):
        l[j] = j
    for j in range(0, m):
        a, b = map(int, input().split())
        if(l[a] < l[b]):
            temp = l[b]
            for p in range(0, n):
                if(l[p] == temp):
                    l[p] = l[a]
        elif(l[b] < l[a]):
            temp = l[a]
            for p in range(0, n):
                if(l[p] == temp):
                    l[p] = l[b]
    q = int(input())
    for p in range(0, q):
        x, y = map(int, input().split())
        if(l[x] == l[y]):
            print("YO")
        else:
            print("NO")
