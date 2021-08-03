class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name is None or len(name) == 0:
            return True

        index = 0
        index2 = 0

        while index < len(name) and index2 < len(typed):

            if name[index] == typed[index2]:
                index += 1
                index2 += 1
            elif name[index] != typed[index2] and index > 0 and name[index - 1] == typed[index2]:
                index2 += 1
            else:
                return False

        while index2 < len(typed):
            if name[len(name) - 1] == typed[index2]:
                index2 += 1
            else:
                return False

        return index == len(name)
