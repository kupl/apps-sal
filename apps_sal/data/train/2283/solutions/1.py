from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    n,sa,sb,a,b = map(int,input().split())
    sa -=1
    sb -=1
    nbr = [[] for i in range(n)]
    for i in range(n-1):
        x, y = map(int,input().split())
        x -= 1
        y-= 1
        nbr[x].append(y)
        nbr[y].append(x)
    if 2 * a >= b:
        print("Alice")
    else:
        #jak najwieksza odleglosc > 2*a to bob, inaczej alice
        q = [sa]
        ind = 0
        dist = [-1] * n
        dist[sa] = 0
        while q:
            if ind >= len(q):
                break
            v = q[ind]
            ind += 1
            for w in nbr[v]:
                if dist[w] == -1:
                    q.append(w)
                    dist[w] = dist[v] + 1
        if dist[sb] <= a:
            print("Alice")
        else:
            q = [0]
            ind = 0
            dist = [-1] * n
            dist[0] = 0
            while q:
                if ind >= len(q):
                    break
                v = q[ind]
                ind += 1
                for w in nbr[v]:
                    if dist[w] == -1:
                        q.append(w)
                        dist[w] = dist[v] + 1
            maksik = 0
            best = 0
            for i in range(n):
                if dist[i] > maksik:
                    best = i
                    maksik = dist[i]
            q = [best]
            ind = 0
            dist = [-1] * n
            dist[best] = 0
            while q:
                if ind >= len(q):
                    break
                v = q[ind]
                ind += 1
                for w in nbr[v]:
                    if dist[w] == -1:
                        q.append(w)
                        dist[w] = dist[v] + 1
            if max(dist) > 2*a:
                print("Bob")
            else:
                print("Alice")
