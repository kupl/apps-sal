class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for a in arr:
            if a not in count:
                count[a] = 1
            else:
                count[a] += 1
        occ = []
        for c in list(count.values()):
            if c not in occ:
                occ.append(c)
            else:
                return False
        return True
