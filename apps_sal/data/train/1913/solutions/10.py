class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if A == []:
            return []
        last = float('inf')
        flag = False
        for i in range(len(A) - 1, -1, -1):
            if A[i] > last:
                flag = True
                break
            last = A[i]
        if not flag:
            return A
        else:
            maxx = -float('inf')
            champ = None
            for j in range(i + 1, len(A)):
                if A[j] > maxx and A[j] < A[i]:
                    champ = j
                    maxx = A[j]
            A[i], A[champ] = A[champ], A[i]

            return A
