class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        d = {}
        for (a, b) in dislikes:
            if a not in d:
                d[a] = []
            d[a].append(b)
            if b not in d:
                d[b] = []
            d[b].append(a)
        vals = [-1] * (N + 1)
        for i in range(1, N + 1):
            if vals[i] != -1:
                continue
            vals[i] = 0
            queue = [i]
            while queue:
                temp = []
                for e in queue:
                    for child in d.get(e, []):
                        if vals[e] == vals[child]:
                            return False
                        if vals[child] == -1:
                            vals[child] = 1 - vals[e]
                            temp.append(child)
                queue = temp
        return True
