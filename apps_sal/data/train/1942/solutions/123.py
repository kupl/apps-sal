class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        return [pid for pid in range(len(favoriteCompanies)) if all((not set(favoriteCompanies[pid]).issubset(s) for s in [a for a in favoriteCompanies if a != favoriteCompanies[pid]]))]
