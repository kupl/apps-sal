class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        last = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hh, mm = time.split(\":\")
            last[name].append(int(hh)*60+int(mm))
            
        ans = []
        for name, times in last.items():
            times.sort()
            l, r = 0, 0
            for r in range(len(times)):
                if r-l >= 2 and times[r]-times[l] <= 60:
                    ans.append(name)
                    break
                while l < r and times[r]-times[l] > 60:
                    l += 1
        return sorted(ans)
