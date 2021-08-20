class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        keyTime = [time.split(':') for time in keyTime]
        keyTime = [[int(time[0]), int(time[1])] for time in keyTime]
        (lru, res) = (defaultdict(deque), set())
        for (name, time) in sorted(zip(keyName, keyTime), key=lambda k: k[1]):
            if name in res:
                continue
            lru[name].append(time)
            if len(lru[name]) > 2:
                (front, mid, back) = (lru[name][0], lru[name][1], lru[name][-1])
                if back[0] == front[0] or (back[0] - front[0] == 1 and back[1] <= front[1]):
                    print((front, mid, back))
                    res.add(name)
                else:
                    lru[name].popleft()
        return sorted(list(res))
