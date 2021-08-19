class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()  # split(sep=None) will discard empty strings.
        cnt = len(words)
        spaces = text.count(' ')
        gap = 0 if cnt == 1 else spaces // (cnt - 1)
        trailing_spaces = spaces if gap == 0 else spaces % (cnt - 1)
        return (' ' * gap).join(words) + ' ' * trailing_spaces
