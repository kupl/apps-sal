from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        subset = Counter()
        for b in B:
            for k, v in Counter(b).items():
                subset[k] = max(subset[k], v)
        result = filter(lambda a: True if not subset-Counter(a) else False, A)
        return list(result)
