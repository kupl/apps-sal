class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        arr = sorted(zip(keyName, keyTime), key=lambda x: self.convert(x[1]))
        times = defaultdict(list)
        ans = set()
        for (name, time) in arr:
            time = self.convert(time)
            if name not in ans:
                if len(times[name]) >= 2 and abs(time - min(times[name])) <= 60:
                    ans.add(name)
                    continue
                times[name].append(time)
                times[name].sort()
                while times[name][-1] - times[name][0] > 60:
                    times[name].pop(0)
        return sorted(ans)

    def convert(self, time):
        hours = 60 * int(time[0:2])
        minutes = int(time[3:5])
        return hours + minutes
