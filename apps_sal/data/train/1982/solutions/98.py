class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        relations = [None] * N
        for x in range(len(relations)):
            relations[x] = []

        for x in dislikes:
            a = min(x) - 1
            b = max(x) - 1
            relations[a].append(b)
            relations[b].append(a)

        colors = [0] * (N)
        for i, v in enumerate(relations):
            q = []
            if colors[i] == 0:
                q.append((i, 1))
            while q:
                (curr, selectedColor) = q.pop(0)
                if colors[curr] != 0:
                    if colors[curr] != selectedColor:
                        return False
                    continue
                colors[curr] = selectedColor
                for n in relations[curr]:
                    q.append((n, -selectedColor))
        return True
