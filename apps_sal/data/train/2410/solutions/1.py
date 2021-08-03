class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if name == typed:
            return True
        if len(set(name)) != len(set(typed)):
            return False
        if len(typed) <= len(name):
            return False
        i = 0
        j = 0
        while j < len(typed) and i < len(name):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j] == typed[j - 1] and j != 0:
                    j += 1
                else:
                    return False

        if i == len(name):
            i = i - 1
        if j == len(typed):
            j = j - 1
        return name[i] == typed[j]
