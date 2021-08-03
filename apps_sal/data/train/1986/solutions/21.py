class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        used = {start}
        two = [2**i for i in range(n)]
        res = [start]

        while len(res) < 2**n:
            i = 0
            a = res[-1] ^ two[i]
            while a in used:
                i += 1
                a = res[-1] ^ two[i]

            used.add(a)
            res.append(a)
        return res
