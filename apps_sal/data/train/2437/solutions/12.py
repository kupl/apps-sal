class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        arrstr = [str(v) for v in arr]
        patterns = defaultdict(int)
        start = end = 0
        n = len(arrstr)

        while end < n:
            if (end - start) + 1 > m:
                start += 1

            if (end - start) + 1 == m:
                substring = ','.join(arrstr[start:end + 1])
                pstart = start - m
                if pstart >= 0 and ','.join(arrstr[pstart:start]) == substring:
                    patterns[substring] += 1
                else:
                    patterns[substring] = 1
                if patterns[substring] >= k:
                    return True
            end += 1

        return False
