class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ret = []
        bx = Counter()
        for ib in B:
            bx |= Counter(ib)

        for ia in A:
            cx = Counter(ia) & bx
            if(cx == bx):
                ret.append(ia)

        return ret
