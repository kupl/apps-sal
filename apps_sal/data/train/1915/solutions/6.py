from collections import deque


class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        (list_s, list_t) = (list(stamp), list(target))
        res = []
        changed = True
        while changed:
            changed = False
            for i in range(len(list_t) - len(list_s) + 1):
                changed = changed or self.remove_stamp(list_s, list_t, i, res)
        return res[::-1] if list_t == ['?'] * len(list_t) else []

    def remove_stamp(self, list_s, list_t, i, res):
        changed = False
        for j in range(len(list_s)):
            if list_t[i + j] == '?':
                continue
            if list_t[i + j] != list_s[j]:
                return False
            changed = True
        if changed:
            list_t[i:i + len(list_s)] = ['?'] * len(list_s)
            res.append(i)
        return changed
