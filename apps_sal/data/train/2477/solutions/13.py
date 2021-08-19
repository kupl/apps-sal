class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        group = []
        for el in A:
            i = 0
            counter = [dict(), dict()]
            for ch in el:
                if ch not in counter[i]:
                    counter[i][ch] = 1
                else:
                    counter[i][ch] += 1
                i = 1 - i
            if counter not in group:
                group.append(counter)
        return len(group)
