class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        i = j = 0
        while i < len(name) and j < len(typed):
            cnt_i = cnt_j = 0
            while i < len(name) - 1 and name[i] == name[i + 1]:
                i += 1
                cnt_i += 1
            while j < len(typed) - 1 and typed[j] == typed[j + 1]:
                j += 1
                cnt_j += 1
            if cnt_i > cnt_j:
                return False
            if name[i] != typed[j]:
                return False
            i += 1
            j += 1
        if i != len(name) or j != len(typed):
            return False
        return True
