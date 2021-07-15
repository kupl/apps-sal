class Solution:
    def rearrangeBarcodes(self, A: List[int]) -> List[int]:
        count = collections.Counter(A)
        A.sort(key=lambda a: (count[a], a))
        A[1::2], A[::2] = A[0:len(A) // 2], A[len(A) // 2:]
        return A

