class Solution:
    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        d = collections.defaultdict(list)

        for i in range(len(name)):
            c = int(time[i][:2]) * 60 + int(time[i][3:])
            d[name[i]].append(c)
        for i in d:
            d[i].sort()
        ans = []
        for i in d:
            for j in range(len(d[i]) - 2):
                if d[i][j + 2] - d[i][j] <= 60:
                    ans.append(i)
                    break
        ans.sort()
        return ans
