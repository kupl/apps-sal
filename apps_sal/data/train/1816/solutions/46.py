class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def to_minutes(s):
            h, m = list(map(int, s.split(':')))
            return h * 60 + m

        alerts = set()
        m = defaultdict(list)
        for time, name in sorted((to_minutes(time), name) for time, name in zip(keyTime, keyName)):
            times = m[name]
            times.append(time)
            if len(times) >= 3 and times[-3] + 60 >= times[-1]:
                alerts.add(name)
        return sorted(alerts)
