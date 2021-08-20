class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for i in range(N)]
        for (a, b) in dislikes:
            adj_list[a - 1].append(b - 1)
            adj_list[b - 1].append(a - 1)
        colors = [0 for i in range(N)]
        for i in range(N):
            if colors[i] != 0:
                continue
            q = [i]
            exp_color = 1
            while len(q) > 0:
                k = len(q)
                for j in range(k):
                    node = q.pop(0)
                    if colors[node] != 0 and colors[node] != exp_color:
                        return False
                    if colors[node] == exp_color:
                        continue
                    colors[node] = exp_color
                    for x in adj_list[node]:
                        q.append(x)
                exp_color = 3 - exp_color
        return True
