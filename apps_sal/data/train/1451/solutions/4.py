import sys
from collections import deque


def minspan(n, edges):
    nodelist = []
    finale = []
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
            merged = save1 | save2
            nodelist.remove(save1)
            nodelist.remove(save2)
            nodelist.append(merged)
        if len(nodelist) == 1:
            break
    return finale


def main():
    t = int(input())
    for i in range(t):
        (n, m) = [int(item) for item in input().split()]
        e = set()
        elist = []
        for i in range(m):
            (u, v) = [int(item) for item in input().split()]
            elist.append((u, v))
            e.add((u, v))
        finale = set(minspan(n, e))
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
            cf[f[0]].add(f[1])
            cf[f[1]].add(f[0])
        root = 1
        visit = set([root])
        visited = set()
        parent = {}
        while len(visited) < n and len(visit) > 0:
            v = visit.pop()
            d = cf[v]
            visited.add(v)
            for i in d:
                if i not in visited:
                    parent[i] = v
                    pf[v].add(i)
                    visit.add(i)
        leaf = set()
        for (k, v) in cf.items():
            if len(v) == 1:
                leaf.add(k)
        st = [1]
        sc = [1]
        while len(st) < n + 1:
            if len(sc) == 0:
                break
            j = sc.pop()
            for i in pf[j]:
                st.append(i)
                sc.append(i)
        while len(st) != 1:
            g = st.pop()
            h = parent[g]
            pair1 = (g, h)
            pair2 = (h, g)
            if indegree[g] % 2 == 0:
                decided.add(pair1)
                indegree[h] += 1
            else:
                decided.add(pair2)
                indegree[g] += 1
        possible = indegree[root] % 2 == 0
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
