class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def time_to_minutes(time):
            h, m = time.split(':')
            return int(m) + 60 * int(h)

        def time_difference(t1, t2):
            return t2 - t1

        keyTime = [time_to_minutes(t) for t in keyTime]
        keyTime, keyName = zip(*sorted(zip(keyTime, keyName)))

        usage = collections.defaultdict(collections.deque)

        res = set()
        for name, time in zip(keyName, keyTime):

            if name in res:
                continue

            if len(usage[name]) == 2:
                if time_difference(usage[name][0], time) <= 60:
                    res.add(name)
                usage[name].popleft()
                usage[name].append(time)
            else:
                usage[name].append(time)

        return sorted(res)
