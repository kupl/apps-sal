class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        LEN = len(favoriteCompanies)
        ans = []
        for i in range(LEN):
            found = False
            for j in range(LEN):
                if i != j:
                    s1 = set(favoriteCompanies[i])
                    s2 = set(favoriteCompanies[j])
                    if len(s1 & s2) == len(s1):
                        found = True

            if not found:
                ans.append(i)
        return ans
