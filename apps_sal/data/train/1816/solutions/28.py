class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def get_time(time):
            return int(time[:2]) * 60 + int(time[3:])
        map = {}
        for (name, time) in zip(keyName, keyTime):
            if name not in map:
                map[name] = []
            map[name].append(get_time(time))
        ans = []
        for name in sorted(map.keys()):
            times = sorted(map[name])
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    ans.append(name)
                    break
        return ans
