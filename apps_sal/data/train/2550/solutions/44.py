class Solution:

    def lemonadeChange(self, A: List[int]) -> bool:
        if A[0] != 5:
            return False
        if len(A) == 0:
            return True
        dk = {5: 0, 10: 0, 20: 0}
        for i in range(len(A)):
            if A[i] in dk:
                dk[A[i]] += 1
            else:
                dk[A[i]] = 1
            if A[i] == 10:
                if dk[5] < 1:
                    return False
                else:
                    dk[5] -= 1
            if A[i] == 20:
                if dk[5] >= 1 and dk[10] >= 1:
                    dk[5] -= 1
                    dk[10] -= 1
                    continue
                elif dk[5] >= 3:
                    dk[5] -= 3
                else:
                    return False
        return True
