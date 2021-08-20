class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        alerts = set()

        def translate(time):
            (hours, minutes) = time.split(':')
            return 60 * int(hours) + int(minutes)
        sorted_times = sorted(enumerate(map(translate, keyTime)), key=lambda p: p[1])
        counts = collections.defaultdict(int)
        q = collections.deque()
        for (i, time) in sorted_times:
            while len(q) and q[0][0] + 60 < time:
                (_, p) = q.popleft()
                counts[p] -= 1
            p = keyName[i]
            counts[p] += 1
            q.append((time, p))
            if counts[p] >= 3:
                alerts.add(p)
        return sorted(alerts)
