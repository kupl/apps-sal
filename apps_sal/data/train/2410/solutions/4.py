class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_len, typed_len = len(name), len(typed)
        if name == typed:
            return True
        elif name_len >= typed_len:
            return False

        t_left, t_right = 0, 1
        n_left, n_right = 0, 1

        while n_left < name_len and t_left < typed_len:
            while n_right < name_len and name[n_left] == name[n_right]:
                n_right += 1
            while t_right < typed_len and typed[t_left] == typed[t_right]:
                t_right += 1

            if name[n_left] != typed[t_left] or (n_right - n_left) > (t_right - t_left):
                return False
            else:
                n_left, n_right = n_right, n_right + 1
                t_left, t_right = t_right, t_right + 1

        return n_left == name_len and t_left == typed_len
