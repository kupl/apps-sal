from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        \"\"\"
        https://leetcode.com/problems/word-subsets/discuss/175854/C%2B%2BJavaPython-Straight-Forward
        \"\"\"

        count = Counter()

        for b in B:
            count |= Counter(b)

        return [a for a in A if (Counter(a) & count) == count]

