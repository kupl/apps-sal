class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = collections.Counter
        bCnt = cnt()
        for b in B:
            bCnt |= cnt(b)
        return [a for a in A if not (bCnt - cnt(a))]
