class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        def fact(n):
            res = 1
            for i in range(2, n + 1):
                res *= i
            print()
            return res

        def nCr(n, r):
            return int(fact(n) / (fact(n - r) * fact(r)))

        from collections import Counter
        time = [i % 60 for i in time]
        cnt = 0
        freq = Counter(time)

       # print(freq)
        for ele in freq:
            if 60 - ele in freq and not ele == 60 - ele and freq[ele] > 0:
                cnt += freq[ele] * freq[60 - ele]
                freq[ele] = 0

            elif 60 - ele in freq and ele == 60 - ele:
                cnt += nCr(freq[ele], 2)
                # print(nCr(freq[ele],2))
            if ele == 0:
                cnt += nCr(freq[ele], 2)
        return cnt
