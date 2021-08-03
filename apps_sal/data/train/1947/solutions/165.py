class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        A_cnt, B_cnt = [], collections.defaultdict(int)
        for a in A:
            A_cnt += [collections.Counter(a)]
        for b in B:
            b_cnt = collections.Counter(b)
            for key in b_cnt:
                B_cnt[key] = max(B_cnt[key], b_cnt[key])

        ret = []
        for i, a in enumerate(A_cnt):
            valid = True
            for key in B_cnt:
                if a[key] < B_cnt[key]:
                    valid = False
                    break

            if valid:
                ret += [A[i]]

        return ret
