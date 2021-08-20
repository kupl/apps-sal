class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter = [0] * 26
        res = []
        for b in B:
            temp = [0] * 26
            for c in b:
                temp[ord(c) - ord('a')] += 1
            for i in range(26):
                counter[i] = max(counter[i], temp[i])
        for a in A:
            temp = [0] * 26
            for c in a:
                k = ord(c) - ord('a')
                temp[k] += 1
            for i in range(26):
                if temp[i] < counter[i]:
                    break
            else:
                res.append(a)
        return res
