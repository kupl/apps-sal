from collections import deque


class Solution:

    def longestDecomposition(self, text: str) -> int:

        def check(a, b):
            return all([a[i] == b[i] for i in range(len(a))])
        ans = 0
        (l, r) = (deque([]), deque([]))
        for i in range(len(text) // 2):
            l.append(text[i])
            r.appendleft(text[-1 - i])
            if check(l, r):
                ans += 2
                (l, r) = (deque([]), deque([]))
        if len(text) % 2 == 0 and len(l) == len(r) == 0:
            return ans
        else:
            return ans + 1
