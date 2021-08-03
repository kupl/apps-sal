class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        table = {}
        mark = []
        best = 0
        for i in points:
            if i[0] not in table:
                table[i[0]] = [[i[1]], []]
            else:
                if i[1] not in table[i[0]][0]:
                    for j in table[i[0]][0]:
                        if j < i[1]:
                            table[i[0]][1].append((j, i[1]))
                        else:
                            table[i[0]][1].append((i[1], j))
                    table[i[0]][0].append(i[1])
                    if len(table[i[0]][0]) == 2:
                        mark.append(i[0])
        g = {}
        if len(mark) < 2:
            return 0
        for i in mark:
            p = table[i]
            for j in p[1]:
                if j in g:
                    for k in g[j]:
                        temp = abs((k - i) * (j[1] - j[0]))
                        if best == 0 or temp < best:
                            best = temp
                    g[j].append(i)
                else:
                    g[j] = [i]
        return best
