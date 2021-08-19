class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if not stamp or not target:
            return []
        (m, n) = (len(stamp), len(target))
        if m > n:
            return []
        if m == n:
            if stamp == target:
                return [0]
            else:
                return []
        if '?' in target:
            return []
        invalid = []
        invert_idx = [set() for _ in range(n)]
        for i in range(n - m + 1):
            mismatch = set()
            for j in range(m):
                if target[i + j] != '?' and target[i + j] != stamp[j]:
                    mismatch.add(i + j)
                    invert_idx[i + j].add(i)
            invalid.append(mismatch)
        cleared = set()
        seq = []
        visited = set()
        while len(cleared) < n:
            not_found = True
            for i in range(len(invalid)):
                if i not in visited and (not invalid[i]):
                    not_found = False
                    seq.append(i)
                    visited.add(i)
                    for j in range(m):
                        cleared.add(i + j)
                        if invert_idx[i + j]:
                            for k in invert_idx[i + j]:
                                invalid[k].remove(i + j)
                            invert_idx[i + j].clear()
                    break
            if not_found:
                return []
        return seq[::-1]
