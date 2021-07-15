class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_cnt = reduce(lambda a, b: Counter(a) | Counter(b), B)
        return [a for a in A if not b_cnt - Counter(a)]
