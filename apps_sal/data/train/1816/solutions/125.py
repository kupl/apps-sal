class Solution:

    def alertNames(self, names: List[str], times: List[str]) -> List[str]:
        (m, alerts) = ({}, [])

        def minutes(time):
            return int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        for (name, time) in zip(names, times):
            if name not in m:
                m[name] = deque()
            m[name].append(minutes(time))
        for (name, times) in m.items():
            q = deque()
            for time in sorted(times):
                while len(q) and q[0] + 60 < time:
                    q.popleft()
                q.append(time)
                if 3 <= len(q):
                    alerts.append(name)
                    break
        return sorted(alerts)
