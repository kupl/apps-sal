class Solution:
    from collections import defaultdict, deque

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        data = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            data[name].append(t)

        def compare(t1, t2):
            t1 = t1.split(':')
            t2 = t2.split(':')
            if t1[0] == t2[0] and t1[1] < t2[1]:
                return True
            if int(t2[0]) - int(t1[0]) == 1 and t1[1] >= t2[1]:
                return True
            return False

        r = []
        for name, times in list(data.items()):
            times.sort()
            q = deque()
            for t in times:
                if not q:
                    q.append(t)
                else:
                    while q and not compare(q[0], t):
                        q.popleft()
                    q.append(t)
                    if len(q) >= 3:
                        r.append(name)
                        break

        return sorted(r)
