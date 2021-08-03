class Solution:
    def longestAwesome(self, s: str) -> int:
        dic, mask, res = {0: -1}, 0, 1
        for i, ch in enumerate(s):
            mask ^= 1 << int(ch)
            dic.setdefault(mask, i)
            res = max(res, i - min([dic[mask]] + [dic.get(mask ^ (1 << k), float('inf')) for k in range(11)]))
        return res


'''
\"3242415\"
\"12345678\"
\"213123\"
\"00\"
'''
