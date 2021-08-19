class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = {}

        def getP(i: int) -> int:
            if i not in p:
                return -1
            return i if p[i] == i else getP(p[i])
        uf = {}
        index = 0
        for (x, y) in pairs:
            px = getP(x)
            py = getP(y)
            if px == -1 and py == -1:
                p[x] = min(x, y)
                p[y] = min(x, y)
                uf[min(x, y)] = pairs[index]
            elif px == -1:
                uf[py].append(x)
                p[x] = py
            elif py == -1:
                uf[px].append(y)
                p[y] = px
            elif px != py:
                p[px] = min(px, py)
                p[py] = min(px, py)
                uf[min(px, py)] += uf.pop(max(px, py))
            index += 1
        ans = list(s)
        for k in list(uf.keys()):
            st = sorted(set(uf[k]))
            tmp = [s[i] for i in st]
            tmp.sort()
            idx = 0
            for i in st:
                ans[i] = tmp[idx]
                idx += 1
        return ''.join(ans)
