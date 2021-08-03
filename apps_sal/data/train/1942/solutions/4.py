class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        return [i for i, s1 in enumerate(favoriteCompanies)
                if not any(set(s1).issubset(s2) for s2 in favoriteCompanies if s1 is not s2)]
