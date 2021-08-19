class Solution:

    def maxPower(self, s: str) -> int:
        cnt = 0
        current = s[0]
        current_cnt = 1
        for l in s[1:]:
            if l == current:
                current_cnt += 1
            else:
                if current_cnt > cnt:
                    cnt = current_cnt
                current = l
                current_cnt = 1
        if current_cnt > cnt:
            cnt = current_cnt
        return cnt
