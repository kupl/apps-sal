class Solution:

    def circularPermutation(self, n, start):

        def g(x):
            return x ^ x >> 1
        return [start ^ g(i) for i in range(1 << n)]
