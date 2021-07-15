class Solution:
    def count_set_bits(self, n):
        count = 0
        for i in range(32):
            count += (n>>i) & (1)
        return count
    
    def longestAwesome(self, s: str) -> int:
        xormap = dict()
        xormap[0] = -1
        xor = 0
        max_length = 0
        for i in range(len(s)):
            xor = xor ^ (1<<int(s[i]))
            max_length = max(max_length, i - xormap.get(xor, float('Inf')))
            for j in range(10):
                temp_xor = xor ^ (1<<j)
                max_length = max(max_length, i - xormap.get(temp_xor, float('Inf')) )
            xormap[xor] = min(i, xormap.get(xor, float('Inf')))        
        
        return max_length
