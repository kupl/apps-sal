class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            times[name].append(time)
        for name in times:
            times[name].sort()
        ans = set()
        for name in times:
            window = defaultdict(deque)
            for time in times[name]:
                hour, minute = time.split(':')
                minutes = int(hour) * 60 + int(minute)
                window[name].append(minutes)
                while window[name][0] < minutes - 60:
                    window[name].popleft()
                if len(window[name]) > 2:
                    ans.add(name)
        return sorted(ans)
