class Solution:

    def beautifulArray(self, N: int) -> List[int]:
        lst = [1]
        while len(lst) < N:
            tmp1 = [2 * i - 1 for i in lst]
            tmp2 = [2 * i for i in lst]
            tmp1.extend(tmp2)
            lst = [i for i in tmp1 if i <= N]
        return lst
