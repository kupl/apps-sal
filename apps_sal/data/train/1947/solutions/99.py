from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universal_word = Counter()
        for b in B:
            universal_word |= Counter(b)

        result = []
        for a in A:
            if not universal_word - Counter(a):
                result.append(a)

        return result
