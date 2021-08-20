class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        while name:
            (i, j) = (0, 0)
            n = name[0]
            while name and name[0] == n:
                i += 1
                name.pop(0)
            while typed and typed[0] == n:
                j += 1
                typed.pop(0)
            if j < i:
                return False
        if typed:
            return False
        return True
