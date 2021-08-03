from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        lst = []
        for word in A:
            evens = []
            odds = []
            for i, l in enumerate(word):
                if i % 2 == 0:
                    evens.append(l)
                else:
                    odds.append(l)
            lst.append((sorted(evens), sorted(odds)))
        s = []
        for word in lst:
            if word not in s:
                s.append(word)
        return len(s)
