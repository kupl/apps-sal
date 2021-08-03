from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        count = Counter()
        for s in A:
            seven = ''
            sodd = ''
            for i in range(len(s)):
                if i % 2 == 0:
                    seven += s[i]
                else:
                    sodd += s[i]
            count[''.join(sorted(seven)), ''.join(sorted(sodd))] += 1
        # print(count.keys())
        return len(count)
