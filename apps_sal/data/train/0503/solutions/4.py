class K:

    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        return len(self.obj) < len(other.obj)


class Solution:

    def arrangeWords(self, text: str) -> str:
        l = text.split()
        l[0] = l[0].lower()
        l = sorted(l, key=K)
        l[0] = l[0].title()
        return ' '.join(l)
