class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = Counter()
        for i in B:
            cnt |= Counter(i)
        res = []
        for i in A:
            if not cnt - Counter(i):
                res.append(i)
        return res
