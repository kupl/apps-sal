class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) or j < len(typed):
            if i < len(name) and j < len(typed) and name[i] == typed[j]:
                i, j = i + 1, j + 1
            elif i > 0 and j < len(typed) and name[i - 1] == typed[j]:
                j += 1
            else:
                return False
        if i == len(name) and j == len(typed):
            return True
        return False
