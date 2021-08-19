class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        pivot = []
        for q in queries:
            pos = q - 1
            for piv in pivot:
                pos = self.getpos(pos, piv)
            pivot.append(pos)
        return pivot

    def getpos(self, pos, piv):
        if pos > piv:
            return pos
        elif pos == piv:
            return 0
        else:
            return pos + 1
