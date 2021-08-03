class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        columns = [''] * len(A[0])
        for string in A:
            for i, char in enumerate(string):
                columns[i] += char
        count = 0
        for word in columns:
            if word != ''.join(sorted(word)):
                count += 1
        return count
