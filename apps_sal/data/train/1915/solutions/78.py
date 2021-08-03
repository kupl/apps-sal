class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if set(stamp) != set(target):
            return []
        done = set()
        n = len(stamp)
        m = len(target)
        candidates = {i for i in range(m - n + 1)}
        res = []

        def check(i):
            j = 0
            count = 0
            while j < n:
                if i in done:
                    j += 1
                    i += 1
                elif stamp[j] == target[i]:
                    count += 1
                    i += 1
                    j += 1
                else:
                    return False
            return count > 0

        while len(done) < m:
            found = 0
            for i in candidates:
                if check(i):
                    for j in range(i, i + n):
                        done.add(j)
                    res.append(i)
                    found = 1
                    break
            if not found:
                return []
            else:
                candidates.remove(i)

        return res[::-1]
