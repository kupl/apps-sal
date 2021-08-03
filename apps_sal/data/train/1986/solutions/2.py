class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res, s = [], None
        for i in range(1 << n):
            tmp = i ^ (i >> 1)
            res.append(i ^ (i >> 1))
            if tmp == start:
                s = i
        res += res
        return res[s:s + len(res) // 2]
