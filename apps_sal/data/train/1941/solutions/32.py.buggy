
from collections import Counter, deque


def make_bitmask(s):
    val = 0x0000
    for si in s:
        val |= (1 << ord(si) - ord('a'))
    return val


def is_submask(maskA, maskB):
    return maskA == (maskA & maskB)


def debug(n):
    s = \"\"
    for i in range(26):
        if (1 << i) & n:
            s += chr(i + ord('a'))
    return s


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        counts = Counter(map(make_bitmask, words))
        
        ret = [0 for _ in range(len(puzzles))]
        for i, p in enumerate(puzzles):
            queue = deque([(make_bitmask(p[0]), 1)])
            val = 0
            seen = set()
            while queue:
                n, depth = queue.popleft()
                if n not in seen:
                    val += counts[n]
                    seen.add(n)
                while depth < len(p):
                    queue.append((n | make_bitmask(p[depth]), depth + 1))
                    depth += 1
            ret[i] = val
        return ret
