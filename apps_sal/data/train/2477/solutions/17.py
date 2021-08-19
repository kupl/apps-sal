class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        odds = []
        evens = []
        n = len(A[0])
        for s in A:
            de = {}
            do = {}
            for i in range(n):
                if i % 2:
                    if s[i] in de:
                        de[s[i]] += 1
                    else:
                        de[s[i]] = 1
                elif s[i] in do:
                    do[s[i]] += 1
                else:
                    do[s[i]] = 1
            odds.append(do)
            evens.append(de)
        total = []
        i = 0
        while i < len(odds):
            j = i + 1
            while j < len(odds):
                if odds[i] == odds[j] and evens[i] == evens[j]:
                    odds.pop(j)
                    evens.pop(j)
                else:
                    j += 1
            i += 1
        return len(odds)
