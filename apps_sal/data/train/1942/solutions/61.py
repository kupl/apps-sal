class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        s = [set(comp) for comp in favoriteCompanies]
        # turn the companies into sets
        # check that all point have i == j or s1 is not a subset s2
        for i, s1 in enumerate(s):
            if all(i == j or not s1.issubset(s2) for j, s2 in enumerate(s)):
                ans.append(i)
        return ans
