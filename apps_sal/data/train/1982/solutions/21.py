class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        gr = [[] for _ in range(N + 1)]
        A = set()
        B = set()
        for x in dislikes:
            gr[x[0]].append(x[1])
            gr[x[1]].append(x[0])
        done = set()
        qu = []
        for v in range(1, N):
            if v not in done:
                qu.append(v)
                A.add(v)
            while qu:
                y = qu.pop(0)
                if y not in done:
                    if y in A:
                        for x1 in gr[y]:
                            B.add(x1)
                            qu.append(x1)
                    else:
                        for x1 in gr[y]:
                            A.add(x1)
                            qu.append(x1)
                    done.add(y)
                if A.isdisjoint(B) == False:
                    return False
        return A.isdisjoint(B)
