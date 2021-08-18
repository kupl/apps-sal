class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def hm_to_min(s):
            h, m = list(map(int, s.split(':')))
            return h * 60 + m
        kt = list(map(hm_to_min, keyTime))
        c = defaultdict(list)
        for i, k in enumerate(keyName):
            bisect.insort(c[k], kt[i])
        res = []
        for k in c:
            for i in range(2, len(c[k])):
                if c[k][i] - c[k][i - 2] <= 60:
                    res.append(k)
                    break
        return sorted(res)
