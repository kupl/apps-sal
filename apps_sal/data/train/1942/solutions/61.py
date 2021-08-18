class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        s = [set(comp) for comp in favoriteCompanies]
        for i, s1 in enumerate(s):
            if all(i == j or not s1.issubset(s2) for j, s2 in enumerate(s)):
                ans.append(i)
        return ans
