class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        m = collections.defaultdict(list)
        n = len(keyName)
        one_hour = 3600
        for i in range(n):
            # print(datetime.datetime.strptime(keyTime[i], \"%H:%M\"))
            m[keyName[i]].append(datetime.datetime.strptime(keyTime[i], \"%H:%M\"))
        ans = set()
        for k in m:
            v = sorted(m[k])
            # print(v)
            # print(v[1] - v[0])
            for i in range(len(v) - 2):
                if (v[i + 1] - v[i]).total_seconds() <= one_hour and (v[i + 2] - v[i]).total_seconds() <= one_hour:
                    ans.add(k)
                    break
                # print(i, )
        return sorted(ans)
