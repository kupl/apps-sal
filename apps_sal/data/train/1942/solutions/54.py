class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        people = []
        sets = [set(a) for a in favoriteCompanies]
        for (i, a) in enumerate(sets):
            for (j, b) in enumerate(sets):
                if i == j:
                    continue
                if a.issubset(b):
                    break
            else:
                people.append(i)
        return people
