class Solution:
    \"\"\"max/min substring: prefixu sum => O(n)
    https://zxi.mytechroad.com/blog/hashtable/leetcode-1542-find-longest-awesome-substring/
    
    1371. find-the-longest-substring-containing-vowels-in-even-counts
    1542. find-longest-awesome-substring
    \"\"\"
    
    def longestAwesome(self, s: str) -> int:
        res = mask = 0
        pre = [-1] + [len(s)] * 1024
        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)
            for digit in range(10):
                res = max(res, i - pre[mask], i - pre[mask ^ (1 << digit)])
            pre[mask] = min(pre[mask], i)
        return res
