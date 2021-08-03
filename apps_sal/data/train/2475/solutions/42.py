class Solution:
    # check all non-decreasing order exists and find all peaks
    def findAllPeaks(self, A: List[str]) -> set():
        if (len(A[0]) <= 1):
            return set()

        column_number = len(A[0])
        row_number = len(A)

        pre_letter_to_int = [-1 for i in range(column_number)]
        result = set()
        for c in range(column_number):
            for r in range(row_number):
                if ord(A[r][c]) < pre_letter_to_int[c]:
                    # find a peak, pre_letter_to_int
                    result.add(c)
                    break
                else:
                    pre_letter_to_int[c] = ord(A[r][c])
        return result

    def minDeletionSize(self, A: List[str]) -> int:
        return len(self.findAllPeaks(A))
