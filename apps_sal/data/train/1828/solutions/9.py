class Solution:
    def rearrangeBarcodes(self, A: List[int]) -> List[int]:
        c = collections.Counter(A)
        A.sort(key=lambda x: (c[x], x))

        A[1::2], A[::2] = A[:len(A) // 2], A[len(A) // 2:]
        return A
