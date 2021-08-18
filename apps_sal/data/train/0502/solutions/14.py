class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if len(initial) == len(graph):
            m = 0
            r = initial[0]
            for i in initial:
                if m < sum(x == 0 for x in graph[i]):
                    m = sum(x == 0 for x in graph[i])
                    r = i
            return r

        d = collections.defaultdict(list)
        for init in initial:
            q = collections.deque()
            q.append(init)
            visit = set()
            visit.add(init)
            while q:
                virus = q.popleft()
                for i in range(len(graph[virus])):
                    if graph[virus][i] == 0 or i in visit:
                        continue
                    visit.add(i)
                    d[i].append(init)
                    q.append(i)
        res = [0] * len(graph)
        for m in d:
            if len(d[m]) == 1:
                res[d[m][0]] += 1
        print(d)
        if max(res) == 0:
            return min(initial)
        return res.index(max(res))
        '''
        51 of 52 passed, only [1,1,0][1,1,0][0,0,1] with [0,1 2] not passing
        d = collections.defaultdict(list)
        for init in initial:
            q = collections.deque()
            q.append(init)
            visit = set()
            visit.add(init)
            while q:
                virus = q.popleft()
                for i in range(len(graph[virus])):
                    if graph[virus][i] == 0 or i in visit:
                        continue
                    visit.add(i)
                    d[i].append(init)
                    q.append(i)
        res = [0]*len(graph)
        for m in d:
            if len(d[m]) == 1:
                res[d[m][0]] += 1
        print(d)
        if max(res) == 0:
            return min(initial)
        return res.index(max(res))
        '''
