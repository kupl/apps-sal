class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges1 = defaultdict(list)
        edges2 = defaultdict(list)
        for (t, a, b) in edges:
            if t == 3:
                edges1[a - 1].append([0, b - 1])
                edges1[b - 1].append([0, a - 1])
                edges2[a - 1].append([0, b - 1])
                edges2[b - 1].append([0, a - 1])
            elif t == 1:
                edges1[a - 1].append([1, b - 1])
                edges1[b - 1].append([1, a - 1])
            else:
                edges2[a - 1].append([1, b - 1])
                edges2[b - 1].append([1, a - 1])
        dis1 = [0] + [1] * (n - 1)
        dis2 = [0] + [1] * (n - 1)
        m = 0
        que1 = []
        que2 = []
        both = []
        for (a, b) in edges1[0]:
            if a == 0:
                both.append(b)
            else:
                que1.append(b)
        for (a, b) in edges1[0]:
            if a == 0:
                continue
            else:
                que2.append(b)
        while both or que1:
            if both:
                D = both.pop()
                if dis1[D]:
                    m += 1
                    dis1[D] = dis2[D] = 0
                else:
                    continue
            else:
                D = que1.pop()
                if dis1[D]:
                    m += 1
                    dis1[D] = 0
                else:
                    continue
            for (c, dd) in edges1[D]:
                if c:
                    que1.append(dd)
                else:
                    both.append(dd)
            edges1[D] = []
            if dis2[D] == 0:
                for (c, dd) in edges2[D]:
                    if c:
                        que2.append(dd)
        while both or que2:
            if both:
                D = both.pop()
                if dis2[D]:
                    m += 1
                    dis1[D] = dis2[D] = 0
                else:
                    pass
            else:
                D = que2.pop()
                if dis2[D]:
                    m += 1
                    dis2[D] = 0
                else:
                    pass
            for (c, dd) in edges2[D]:
                if c:
                    que2.append(dd)
                else:
                    both.append(dd)
            edges2[D] = []
        print((dis1, dis2))
        if 1 in dis1 or 1 in dis2:
            return -1
        return len(edges) - m
