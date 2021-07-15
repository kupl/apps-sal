class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bLets = collections.Counter()
        for w in B:
            for l, cnt in collections.Counter(w).items():
                if cnt > bLets[l]:
                    bLets[l] = cnt
        bLets = bLets.most_common()
        result = []
        for w in A:
            aLets = collections.Counter(w)
            for l, cnt in bLets:
                if cnt > aLets[l]:
                    break
            else:
                result.append(w)
        return result
