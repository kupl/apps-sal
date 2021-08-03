class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        D = collections.defaultdict(int)

        for i, cs in enumerate(favoriteCompanies):
            p = 1 << i

            for c in cs:
                D[c] |= p

        res = []
        ac = 2 ** len(favoriteCompanies) - 1

        for i, cs in enumerate(favoriteCompanies):
            p = 1 << i
            pc = ac

            for c in cs:
                pc &= D[c]

            if p == pc:
                res.append(i)

        return res
