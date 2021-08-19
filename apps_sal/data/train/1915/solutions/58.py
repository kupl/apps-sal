class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        lens, lent = len(stamp), len(target)
        out = []
        q = collections.deque()
        done = set()
        # create v,t
        v = [set() for _ in range(lent - lens + 1)]
        t = [set() for _ in range(lent - lens + 1)]
        # iterate over all offsets
        for i in range(len(target) - len(stamp) + 1):
            for j in range(len(stamp)):
                if stamp[j] == target[i + j]:
                    v[i].add(i + j)
                else:
                    t[i].add(i + j)
            if len(t[i]) == 0:
                out.append(i)
                for j in range(len(stamp)):
                    done.add(i + j)
                q.append(i)
        while q:
            offset = q.popleft()
            for of in range(max(0, offset - lens + 1), min(lent - lens + 1, offset + lens)):
                t[of] -= done
                if len(t[of]) == 0:
                    if len(v[of] - done) > 0:
                        q.append(of)
                        done |= v[of]
                        out.append(of)
        if len(done) == lent:
            return out[::-1]
        return []
