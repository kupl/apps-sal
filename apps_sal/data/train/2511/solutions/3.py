class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)
        counter = {}
        for num in A:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

            if counter[num] == N // 2:
                return num
