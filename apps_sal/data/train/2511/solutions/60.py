class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        twoN = len(A)
        N = twoN // 2
        unique = N + 1
        hashMap = {}
        for num in A:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        for (key, value) in hashMap.items():
            if value == N:
                return key
