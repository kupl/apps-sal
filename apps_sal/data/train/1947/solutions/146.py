class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dic = {}
        res = []
        for b in B:
            for char in b:
                dic[char] = max(dic.get(char, 0), b.count(char))
        for a in A:
            if all((a.count(k) >= dic[k] for k in dic)):
                res.append(a)
        return res
