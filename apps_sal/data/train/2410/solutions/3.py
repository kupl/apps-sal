class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = 0
        t = 0
        while n < len(name) and t < len(typed):
            if name[n] == typed[t]:
                n += 1
                t += 1
            elif t and typed[t] == typed[t - 1]:
                t += 1
            else:
                return False
        if n != len(name):
            return False
        while t < len(typed):
            if typed[t] == typed[t - 1]:
                t += 1
            else:
                return False
        return True
