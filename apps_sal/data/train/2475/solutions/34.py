class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        count = 0

        for i in range(len(A[0])):
            if not self.isSorted(list([x[i] for x in A])):
                count += 1

        return count

    def isSorted(self, list_char):
        for i in range(1, len(list_char)):
            if list_char[i - 1] > list_char[i]:
                return False

        return True
