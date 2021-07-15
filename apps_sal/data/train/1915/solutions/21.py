class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        if n < m:
            return False

        def check_and_mark(s: list, i: int) -> tuple:
            # return True if update, next_read_pos
            if s[i:i+m] == ['?'] * m:
                return False, i + 1
            i0 = i
            j = 0
            while i < n and j < m and (s[i] == '?' or s[i] == stamp[j]):
                i += 1
                j += 1
            if j == m:
                s[i0:i0 + m] = ['?'] * m
                return True, i
            else:
                return False, (n if i == n else i0 + 1)
        
        final = ['?'] * n
        ans = []
        target = list(target)
        while target != final:
            i = 0
            updated = False
            while i < n:
                done, i = check_and_mark(target, i)
                if done:
                    updated = done
                    ans.append(i - m)
            if not updated:
                return []
        return ans[::-1]
