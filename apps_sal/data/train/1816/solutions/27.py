class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = collections.defaultdict(list)
        ans = set()
        for name, time in sorted(zip(keyName, keyTime), key=lambda x: x[1]):
            if name not in ans:
                h, m = map(int, time.split(':'))
                t = h * 60 + m
                if len(dic[name]) >= 2 and dic[name][-2] >= t - 60:
                    ans.add(name)
                    del dic[name]
                else:
                    dic[name].append(t)
                    dic[name] = dic[name][-2:]
        return sorted(ans)
