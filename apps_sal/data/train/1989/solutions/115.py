class Solution:
    '''
We have 10 + 1 types of palindromes. Use any number as the middle character, or don't have a middle character.

BitMask solution
We don't have to keep track of counters, we are only interested in odd counts in a substring. We can use one bit to say if some digit has even or odd count at any point.
Let 0 represent \"even\" and 1 represent \"odd\".
For example, for an input of \"233\":
i = 0, char = '2', xor 2nd bit from right:
mask = \"100\"
i = 1, char = '3', xor 3rd bit from right:
mask = \"1100\"
i = 2, char = '3', xor 3rd bit from right:
mask = \"0100\"
The last mask is \"0100\" which says it has only one number with odd count, so, the input can be rearranged to make it a palindrome: \"233\" => \"323\".
    '''

    def longestAwesome(self, s: str) -> int:
        n = len(s)
        res = mask = 0
        seen = [n] * 1024
        seen[0] = -1
        for i in range(n):
            mask ^= 1 << int(s[i])
            res = max(res, i - seen[mask])
            for num in range(10):
                res = max(res, i - seen[mask ^ (1 << num)])
            seen[mask] = min(seen[mask], i)
        return res
