import sys
from collections import deque

croot = dict()
setnumber = dict()

def finalroot(v):
    if croot[v] != v:
        v = finalroot(croot[v])
    return v

def union(v1,v2):
    r1 = finalroot(v1)
    r2 = finalroot(v2)
    if r1 != r2:
        if setnumber[r1] > setnumber[r2]:
            croot[r2] = r1
        else:
            croot[r1] = r2
            if setnumber[r1] == setnumber[r2]:
                setnumber[r2] += 1

def minspan(n,edges):

    finale = []
    edgecount = {}

    for i in range(n):
        edgecount[i+1] = 0
        setnumber[i+1] = 0
        croot[i+1] = i+1

    edges.sort()

    for e in edges:
        u,v = e
        if finalroot(u) != finalroot(v):
            edgecount[u] += 1
            edgecount[v] += 1
            finale.append((u,v))
            union(u,v)

    root = max(edgecount.keys(), key=(lambda k: edgecount[k]))
    return set(finale),root

def main():

    t = int(input())

    for i in range(t):

        n,m = [int(item) for item in input().split()]
        e = set()
        elist = []

        for i in range(m):
            u,v = [int(item) for item in input().split()]
            elist.append((u,v))
            e.add((u,v))

        finale,root = minspan(n,list(e))
        sroot = root
        tofix = e - finale

        indegree = {}
        for i in range(n):
            indegree[i+1] = 0

        decided = set()

        # randomly assign directions to edges not in min span
        for t in tofix:
            indegree[t[1]] += 1
            decided.add((t[0],t[1]))

        cf = {}
        pf = {}

        for i in range(n):
            cf[i+1] = set()
            pf[i+1] = set()

        # minspan finale- create tree
        # 2 dics cf - contains each node with it's child
        # pf - each node with it's parent

        for f in finale:
            u,v = f
            cf[u].add(v)
            cf[v].add(u)

        r = deque()
        r.append(root)

        while len(r) != 0:
            root = r.pop()
            for c in cf[root]:
                r.append(c)
                cf[c].remove(root)
                pf[c] = root


        q = deque([sroot])
        st = deque()
        # tree traversal
        while len(q) != 0:
            node = q.pop()
            st.append(node)
            for e in cf[node]:
                q.append(e)

        while len(st) != 0:
            c = st.pop()
            if c != sroot:
                p = pf[c]
                if indegree[c]%2 == 0:
                    #outgoing
                    decided.add((c,p))
                    indegree[p] += 1
                else:
                    decided.add((p,c))
                    indegree[c] += 1

        possible = (indegree[sroot]%2 == 0)
        if possible:
            ans = []
            for i in elist:
                if i in decided:
                    ans.append(0)
                else:
                    ans.append(1)
            print(*ans)
        else:
            print(-1)

    return 0

def __starting_point():
    main()

__starting_point()
