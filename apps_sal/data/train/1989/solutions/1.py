class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        prefix, suffix = {0: -1}, {0: -1}
        digcodes = [2**i for i in range(10)] + [0]

        for i in range(len(s)):
            ch = s[i]
            mask ^= 2**int(ch)
            if mask not in prefix:
                prefix[mask] = i
            suffix[mask] = i

        return max([ind - prefix[val ^ dig] for val, ind in list(suffix.items())
                    for dig in digcodes if val ^ dig in prefix])
