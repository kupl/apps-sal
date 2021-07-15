class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        group = [None] * (N + 1)
        group[dislikes[0][0]] = 1
        group[dislikes[0][1]] = -1
        counter = 2
        for i, j in dislikes[1:]:
            if group[i] and group[j]:
                if group[i] == group[j]:
                    return False
                if group[i] * group[j] > 0:
                    l = group[j]
                    for k in range(N + 1):
                        if group[k] == l:
                            group[k] = -group[i]
                        if group[k] == -l:
                            group[k] = group[i]
            if not group[i] and not group[j]:
                group[i], group[j] = counter, -counter
                counter += 1
                continue
            if group[i]:
                group[j] = -group[i]
            if group[j]:
                group[i] = -group[j]
        return True
