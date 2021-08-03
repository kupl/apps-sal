class Solution:
    def getStrongest(self, A: List[int], k: int) -> List[int]:
        A.sort()
        z = []
        if len(A) % 2 == 1:
            n = A[(len(A) - 1) // 2]
        else:
            n = A[len(A) // 2 - 1]
        for i in A:
            z.append([abs(i - n), i])
        z.sort(key=lambda x: x[0])
        x = [j for i, j in z]
        return x[len(x) - k:]
