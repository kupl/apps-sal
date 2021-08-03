class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic = collections.defaultdict(list)
        for n, t in zip(keyName, keyTime):
            dic[n].append(datetime.datetime.strptime(t, \"%H:%M\"))
        ans = []
        for n in dic:
            dic[n].sort()
            j = 0
            cur = 0
            for i, t in enumerate(dic[n]):
                while (t - dic[n][j]).seconds > 3600:
                    j += 1
                if i - j + 1 >= 3:
                    ans.append(n)
                    break
        return sorted(ans)
