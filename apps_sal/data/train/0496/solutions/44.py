class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A.append(100000)
        result = taken = 0
        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                taken += 1
                result -= A[i]
            else:
                give = min(taken, A[i] - A[i - 1] - 1)
                result += give * (give + 1) // 2 + give * A[i - 1]
                taken -= give
        return result
        counter = collections.Counter(A)
        taken = []
        result = 0
        for i in range(100000):
            if counter[i] > 1:
                taken.extend([i] * (counter[i] - 1))
            elif taken and counter[i] == 0:
                result += i - taken.pop()
        return result
