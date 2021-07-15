from collections import defaultdict
class Solution:
    # 先分析题目，一段substr如果可以通过swap形成一个palindrome，说明里面的所有数字要么都是偶数(e.g. 240042)，要么有且只能有一个奇数(e.g. 2401042)
    # 这样就需要用bitmask，用一个10位二进制数表示，第i位如果是0说明substr里有偶数个i，第i位如果是1说明substr里有奇数个i
    # 每次substr向右扩展一个数j，就把当前mask xor (1 << j), 即可完成上述奇偶变化
    # intuitive solution: top-down dp，答案在最下，超时
    # bottom-up dp solution: time O(n*1024), space O(1024)
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        dp = [n for i in range(1024)]
        dp[0] = -1
        mask, ret = 0, 0
        
        for i, c in enumerate(s):
            mask ^= (1 << int(c))
            for num in range(10):
                ret = max(ret, i-dp[mask^(1<<num)])
            ret = max(ret, i-dp[mask])
            dp[mask] = min(dp[mask], i)
        return ret
        
        
#     def longestAwesome(self, s: str) -> int:
#         n = len(s)
#         M = defaultdict(int)
        
#         def count(mask):
#             counter = 0
#             while mask:
#                 mask &= mask-1
#                 counter += 1
#             return counter
        
#         # 定义dp(l, r, mask)为s[l, r]包含的最长awesome substr
#         def dp(l, r, mask):
#             if l > r:
#                 return 0
            
#             if (l, r, mask) in M:
#                 return M[(l, r, mask)]
            
#             if count(mask) <= 1:
#                 M[(l, r, mask)] = r-l+1
            
            
            
#             if r+1 < n:
#                 new_mask = mask ^ (1 << int(s[r+1]))
#                 M[(l, r, mask)] = max(M[(l, r, mask)], dp(l, r+1, new_mask))
#             if l+1 < n:
#                 new_mask = mask ^ (1 << int(s[l])) 
#                 M[(l, r, mask)] = max(M[(l, r, mask)], dp(l+1, r, new_mask))
            
#             return M[(l, r, mask)]
        
#         dp(0, 0, 1<<int(s[0]))
#         return M[(0, 0, 1<<int(s[0]))]

