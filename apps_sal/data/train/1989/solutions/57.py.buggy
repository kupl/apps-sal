\"\"\"
the character w/ odd count must be no longer than 1
for a given character
freq[i:j] = prefix[j] - prefix[i-1]

1. all characters: count are even
2. only one character: count is odd

with prefix[i-1] is odd/even known, we'd like to know the smallest i
key: odd/even of prefix, value : idx
prefix[j] : 1000001 -> prefix[i-1] : 1000001
prefix[j] : 1000001 -> prefix[i-1] : 0000001
                                     1100001
                                     1100001

\"\"\"


class Solution:
    def longestAwesome(self, s: str) -> int:
        table = {0 : -1}
        count = [0] * 10
        res = 0
        for i in range(len(s)):
            count[int(s[i])] += 1
            key = self.convert(count)
            if key in table:
                res = max(res, i - table[key])            
            for k in range(10):
                newKey = key
                if ((key>>k)&1)==0:
                    newKey += (1<<k)
                else:
                    newKey -= (1<<k)
                if newKey in table:
                    res = max(res, i - table[newKey])
            if key not in table:
                table[key] = i
        return res
        
    def convert(self, count):
        key = 0
        for i in range(10):
            key += ((count[i]%2)<<i)
        return key
        
        
        
