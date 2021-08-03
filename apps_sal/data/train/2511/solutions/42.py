class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        for i in range(0, len(A)):
            new = [A[i]]
            for j in range(i + 1, len(A)):
                if (A[i] == A[j]):
                    new.append(A[i])
                    if len(new) == len(A) / 2:
                        print(new)
                        return A[i]
