class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        group = [None] * (N + 1)
        group[dislikes[0][0]] = 1
        group[dislikes[0][1]] = -1
        group1 = set([1])
        group2 = set()
        counter = 2
        for i, j in dislikes[1:]:
            if group[i] and group[j]:
                if group[i] == group[j]:
                    return False
                if group[i] in group1:
                    if group[j] in group1 or -group[j] in group2:
                        return False
                    group2.add(group[j])
                elif group[i] in group2:
                    if group[j] in group2 or -group[j] in group1:
                        return False
                    group1.add(group[j])
                elif group[j] in group1:
                    if group[i] in group1 or -group[i] in group2:
                        return False
                    group2.add(group[i])
                elif group[j] in group2:
                    if group[i] in group2 or -group[i] in group1:
                        return False
                    group1.add(group[i])
            elif not group[i] and not group[j]:
                group[i], group[j] = counter, -counter
                counter += 1
            elif group[i]:
                group[j] = -group[i]
            elif group[j]:
                group[i] = -group[j]
        return True
