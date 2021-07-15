class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # 'a' 1
        # 'aa' 1
        # 'ab' 2
        # 'abb' 2
        # 'aabb' 2
        # 'abba' 1
        # 'abaaba'
        
        if len(s) == 0:
            return 0
        if s == s[::-1]:
            return 1
        return 2
