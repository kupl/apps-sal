
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        idx = 0

        name_len, typed_len = len(name), len(typed)

        for i, val in enumerate(typed):
            if idx < name_len and name[idx] == val:
                idx += 1

            elif i == 0 or typed[i] != typed[i - 1]:
                return False

        return idx == name_len
