class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        rear = len(A) - 2
        while rear > -1:
            if A[rear] > A[rear + 1]:
                break
            rear -= 1
        if rear == -1:
            return A
        front = len(A) - 1
        while A[front] >= A[rear] or A[front - 1] == A[front]:
            front -= 1
        A[rear], A[front] = A[front], A[rear]
        return A
