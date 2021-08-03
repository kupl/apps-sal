class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = []
        for t in keyTime:
            t = t.split(\":\")
            times.append([int(t[0]), int(t[1])])
        name_time = sorted(zip(keyName, times), key=lambda x: (x[0], x[1][0], x[1][1]))
        ans = set()
        for i in range(len(name_time) - 2):
            name = name_time[i][0]
            time = name_time[i][1]
            nname = name_time[i + 2][0]
            ntime = name_time[i + 2][1]
            if name == nname:
                during = (ntime[0] - time[0]) * 60 + (ntime[1] - time[1])
                if during <= 60:
                    ans.add(name)
        
        ans = sorted(list(ans))
        
        return ans
