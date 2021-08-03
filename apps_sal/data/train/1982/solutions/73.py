class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        h = collections.defaultdict(list)
        if dislikes == []:
            return True
        for i in dislikes:
            h[i[0]].append(i[1])
            h[i[1]].append(i[0])
        k = set()
        for j in list(h.keys()):
            if j in k:
                continue
            v = set()
            c = set()
            q = deque()
            q.append((j, 1))
            while q:
                x = q.popleft()
                if x[0] in v:
                    if x[0] in c:
                        if x[1] == 1:
                            continue
                        else:
                            return False
                    else:
                        if x[1] == 2:
                            continue
                        else:
                            return False
                v.add(x[0])
                k.add(x[0])
                if x[1] == 1:
                    c.add(x[0])
                for i in h[x[0]]:
                    if x[1] == 1:
                        q.append((i, 2))
                    else:
                        q.append((i, 1))
        return True
