class Solution:
    def longestAwesome(self, s: str) -> int:
        # we need to find longest substring such that
        # at most one digit has odd number of occurrences
        # we can use XOR to compute whether there is an odd # of each digit

        # map current n representing odd/even occurrences of each digit
        # to earliest seen position
        # if n == 0, then palindrome length is whole string
        seen = {0: -1}
        max_len = 0

        n = 0
        for i in range(len(s)):
            digit = int(s[i])
            n = n ^ (1 << digit)
            # print(digit, n)

            if n in seen:
                max_len = max(max_len, i - seen[n])

            for start in range(10):
                m = n ^ (1 << start)
                if m in seen:
                    max_len = max(max_len, i - seen[m])

            if n not in seen:
                seen[n] = i

        return max_len
