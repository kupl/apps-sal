import collections


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        bcount = collections.defaultdict(int)
        for s in B:
            counter = collections.Counter(s)
            for c in list(counter.keys()):
                if bcount[c] < counter[c]:
                    bcount[c] = counter[c]
        for s in A:
            counter = collections.Counter(s)
            flag = True
            for c in list(bcount.keys()):
                if not counter[c] >= bcount[c]:
                    flag = False
                    break
            if flag:
                res.append(s)
        return res
