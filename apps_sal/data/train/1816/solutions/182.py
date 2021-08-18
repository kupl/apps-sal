class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict

        d = defaultdict(list)
        n = len(keyName)

        for i in range(n):
            time = int(keyTime[i][:1] + keyTime[i][3:])
            d[keyName[i]].append(int(keyTime[i][:2] + keyTime[i][3:]))

        ans = []

        for name in d:
            d[name].sort()

            for i in range(len(d[name]) - 2):
                if d[name][i + 2] - d[name][i] <= 100:
                    ans.append(name)
                    break

        print(d)

        return sorted(ans)
