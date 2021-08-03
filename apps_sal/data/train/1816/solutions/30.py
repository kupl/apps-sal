class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict, deque
        maps = defaultdict(deque)

        res = set()
        for name, time in sorted(zip(keyName, keyTime)):
            h = int(time[:2])
            m = int(time[3:])
            t = h * 60 + m

            queue = maps[name]
            while queue and queue[0][0] * 60 + queue[0][1] < t - 60:
                queue.popleft()
            queue.append([h, m])

            if len(queue) >= 3:
                res.add(name)
        return sorted(res)
