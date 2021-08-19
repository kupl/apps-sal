class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def calcmin(t: str) -> int:
            return int(t[:2]) * 60 + int(t[3:])
        (key, res) = ({}, [])
        for (i, v) in enumerate(keyName):
            if not v in key:
                key[v] = []
            key[v] += [keyTime[i]]
        for k in key:
            key[k].sort()
            for i in range(2, len(key[k])):
                if calcmin(key[k][i]) - calcmin(key[k][i - 2]) <= 60:
                    res += [k]
                    break
        return sorted(res)
