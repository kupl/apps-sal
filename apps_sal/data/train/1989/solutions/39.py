class Solution:
    def longestAwesome(self, s: str) -> int:
        res = 0
        count = 0
        record = {count:-1}
        for i,ss in enumerate(s):
            count ^= 1<<int(ss)
            if count not in record:
                record[count] = i
            res = max(res, max((i - record[count^(1<<(t+1)>>1)]) if count^(1<<(t+1)>>1) in record else 0 for t in range(-1,10)))
        return res

