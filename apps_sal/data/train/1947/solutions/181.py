class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        book = collections.defaultdict(int)
        for b in B:
            book2 = Counter(b)
            for bb in book2:
                book[bb] = max(book[bb], book2[bb])

        res = []
        for a in A:
            aa = Counter(a)
            if all(k in aa and aa[k] >= book[k] for k in book):
                res.append(a)
        return res
