class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        d1 = collections.defaultdict(lambda: [])
        d2 = collections.defaultdict(lambda: [])
        d3 = collections.defaultdict(lambda: [])

        count = [0] * 4
        for e in edges:
            t = e[0]
            u = e[1]
            v = e[2]

            if t == 1:
                d1[u].append(v)
                d1[v].append(u)
            elif t == 2:
                d2[u].append(v)
                d2[v].append(u)
            else:
                d1[u].append(v)
                d1[v].append(u)
                d2[u].append(v)
                d2[v].append(u)
                d3[u].append(v)
                d3[v].append(u)
            count[t] += 1

        print(count)
        # print(d1)
        # print(d2)
        # print(d3)

        def check(d):
            visited = [False] * (n + 1)
            self.sz = 0

            def trav(i):
                if visited[i] == True:
                    return
                self.sz += 1
                visited[i] = True
                # print(d[i])
                for j in d[i]:
                    trav(j)
            trav(1)
            #print(visited, self.sz)
            return self.sz == n

        if(not check(d1)):
            return -1

        if(not check(d2)):
            return -1

        comps = 0

        visited = [False] * (n + 1)

        def travers(x):
            if visited[x] == True:
                return

            visited[x] = True
            for y in d3[x]:
                travers(y)

        for i in range(1, n + 1):
            if visited[i] == False:
                comps += 1
                travers(i)
            #print(i, comps)
        print(('comps', comps))

        print(((count[1] - comps + 1), (count[2] - comps + 1), count[3] - n + comps))
        return (count[1] - comps + 1) + (count[2] - comps + 1) + count[3] - n + comps
