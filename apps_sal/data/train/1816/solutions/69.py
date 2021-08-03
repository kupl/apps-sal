class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            times[name].append(time)
        res = []

        def withinOneHour(t1, t2):
            (h1, m1) = [int(i) for i in t1.split(':')]
            t1 = h1 * 60 + m1
            (h2, m2) = [int(i) for i in t2.split(':')]
            t2 = h2 * 60 + m2
            return t2 - t1 <= 60
        for name in sorted(times):
            time = sorted(times[name])
            queue = []
            for t in time:
                queue.append(t)
                if not withinOneHour(queue[0], queue[-1]):
                    queue.pop(0)
                if len(queue) >= 3:
                    res.append(name)
                    break
        return res
