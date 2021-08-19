class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        if not B:
            return A
        mapB = [0] * 26
        B = list(set(B))
        for b in B:
            if not b:
                continue
            counter = collections.Counter(b)
            for k in b:
                index = ord(k) - ord('a')
                if counter[k] > mapB[index]:
                    mapB[index] = counter[k]
        print(mapB)
        res = []
        for a in A:
            temp = mapB[:]
            for c in a:
                i = ord(c) - ord('a')
                if temp[i] > 0:
                    temp[i] -= 1
            if sum(temp) == 0:
                res.append(a)
        return res
