class Solution:
    def longestAwesome(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len = 1
        # p[i] contains a 10-bit number where the k-th bit of p[i] is 0 if there are
        # even instances of digit k in s[0..i], or k-th bit of p[i] is 1 if there are
        # odd instances of digit k in s[0..i].
        p = [0] * len(s)
        # seen[x] holds the smallest index at which some p[i] == x was seen. We can therefore
        # query `seen` to find out when some odd/evenness digit instance state was first seen.
        # For convinience, we can say we've seen even instances of all digits [0-9] at index
        # -1, ie. we've seen zero instances of every digit before index 0
        seen = {0: -1}
        for i in range(0, len(s)):
            d = ord(s[i]) - ord('0')
            p[i] = (1 << d) ^ p[i - 1]

            # To make a palindrome, we can only have at most one digit with odd number of instances.
            # We'll go through every possible digit and designate that digit as the special digit
            # and see that if we can subtract previously seen instances of digits to make a valid
            # palindrome.
            for sd in range(10):
                # If some previous instance \"state\" has odd instances of `sd` for s[0..i'], i' < i,
                # then s[0..i] can have either even or odd instances of `sd`, as long as s[0..i]
                # has the same odd/even instances for all other digits. (for `sd`, we'd have odd-odd
                # instances or even-odd instances, which is even or odd instances of `sd`; for all
                # other digits, we'd have odd-odd or even-even instances, which is even instances
                # for all other digits)
                x = p[i] | (1 << sd)  # bit represending `sd` is set to 1, indicating odd
                if x in seen:
                    max_len = max(max_len, i - seen[x])

                # If some previous instance \"state\" has even instances of `sd` for s[0..i'], i' < i,
                # then s[0..i] can have either even or odd instances of `sd`, as long as s[0..i]
                # has the same odd/even instances for all other digits.
                y = p[i] & (~(1 << sd))  # bit represending `sd` is set to 0, indicating even
                if y in seen:
                    max_len = max(max_len, i - seen[y])

            if p[i] not in seen:
                seen[p[i]] = i

        return max_len
