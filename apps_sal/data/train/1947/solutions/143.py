class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bLets = collections.Counter()
        for w in B:
            for l, cnt in collections.Counter(w).items():
                if cnt > bLets[l]:
                    bLets[l] = cnt
        bTotal = sum(bLets.values())
        bLets = bLets.most_common()
        result = []
        aLets = collections.Counter()
        for w in A:
            if len(w) >= bTotal:
                aLets.update(w)
                for l, cnt in bLets:
                    if cnt > aLets[l]:
                        break
                else:
                    result.append(w)
                aLets.clear()
        return result
