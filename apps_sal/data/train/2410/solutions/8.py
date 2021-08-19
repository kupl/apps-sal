class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        (l, r) = (0, 0)
        (n, m) = (len(name), len(typed))
        last = None
        while l < n and r < m:
            if name[l] == typed[r]:
                last = name[l]
                l += 1
                r += 1
            elif last and typed[r] == last:
                r += 1
            else:
                return False
        if l == n:
            while r < m:
                if typed[r] == last:
                    r += 1
                else:
                    return False
            return True
        return False
