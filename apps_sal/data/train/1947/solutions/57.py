class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dic = {}
        for b in B:
            for char in b:
                dic[char] = max(dic.get(char, 0), b.count(char))
        res = []
        for a in A:
            if all((a.count(k) >= dic[k] for k in dic)):
                res.append(a)
        return res
