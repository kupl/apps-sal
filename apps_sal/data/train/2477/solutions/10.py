from collections import defaultdict


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = []
        for word in A:
            result = {0: defaultdict(int), 1: defaultdict(int)}
            for i, char in enumerate(word):
                result[i % 2][char] += 1
            if result not in groups:
                groups.append(result)
        return len(groups)
