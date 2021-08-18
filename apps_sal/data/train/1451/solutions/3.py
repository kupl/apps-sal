import sys
from collections import deque


def minspan(n, edges):

    nodelist = []
    finale = []
    edgecount = {}

    for i in range(n):
        edgecount[i + 1] = 0

    for i in range(n):
        nodelist.append(set([i + 1]))

    for e in edges:

        u = e[0]
        v = e[1]

        for each_set in nodelist:
            if u in each_set:
                save1 = each_set
            if v in each_set:
                save2 = each_set

        if save1 != save2:
            finale.append((u, v))
            edgecount[u] += 1
            edgecount[v] += 1
            merged = save1 | save2
            nodelist.remove(save1)
            nodelist.remove(save2)
            nodelist.append(merged)

        if len(nodelist) == 1:
            break

    root = max(edgecount.keys(), key=(lambda k: edgecount[k]))
    return set(finale), root


def main():

    t = int(input())

    for i in range(t):

        n, m = [int(item) for item in input().split()]
        e = set()
        elist = []

        for i in range(m):
            u, v = [int(item) for item in input().split()]
            elist.append((u, v))
            e.add((u, v))

        finale, root = minspan(n, e)
        sroot = root
        tofix = e - finale

        indegree = {}
        for i in range(n):
            indegree[i + 1] = 0

        decided = set()

        for t in tofix:
            indegree[t[1]] += 1
            decided.add((t[0], t[1]))

        cf = {}
        pf = {}

        for i in range(n):
            cf[i + 1] = set()
            pf[i + 1] = set()

        for f in finale:
            u, v = f
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
        while len(q) != 0:
            node = q.pop()
            st.append(node)
            for e in cf[node]:
                q.append(e)

        while len(st) != 0:
            c = st.pop()
            if c != sroot:
                p = pf[c]
                if indegree[c] % 2 == 0:
                    decided.add((c, p))
                    indegree[p] += 1
                else:
                    decided.add((p, c))
                    indegree[c] += 1

        possible = (indegree[sroot] % 2 == 0)
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
