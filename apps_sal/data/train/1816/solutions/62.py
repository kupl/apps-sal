class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def get_diff_minutes(t1, t2):
            h1, m1 = t1.split(':')
            h2, m2 = t2.split(':')
            return (int(h2) - int(h1)) * 60 + int(m2) - int(m1)

        res = set()
        store = defaultdict(deque)
        for time, name in sorted(zip(keyTime, keyName)):
            # print(name, time)
            while store[name] and get_diff_minutes(store[name][0], time) > 60:
                store[name].popleft()
            store[name].append(time)
            if len(store[name]) >= 3:
                res.add(name)

        # print(res)
        return sorted(res)
