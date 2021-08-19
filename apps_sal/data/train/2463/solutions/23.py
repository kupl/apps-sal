class Solution:

    def walkUp(self, A: List[int]) -> int:
        for (i, step) in enumerate(A[:-1]):
            if A[i] >= A[i + 1]:
                return i
        return len(A)

    def walkDown(self, A: List[int], top: int) -> bool:
        for (i, step) in enumerate(A[top:-1], start=top):
            if A[i] <= A[i + 1]:
                return False
        return True

    def validMountainArray(self, A: List[int]) -> bool:
        top = self.walkUp(A)
        if top == 0 or top == len(A):
            return False
        return self.walkDown(A, top)
