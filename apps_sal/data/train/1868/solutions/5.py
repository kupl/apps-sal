class Solution:
    def beautifulArray(self, N: int) -> List[int]:

        res = [1]

        while len(res) < N:
            tmp = []
            for num in res:
                if num * 2 - 1 <= N:
                    tmp.append(num * 2 - 1)
            for num in res:
                if num * 2 <= N:
                    tmp.append(num * 2)
            res = tmp

        return res
