class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        i = 0
        ans = []
        
        while i < len(favoriteCompanies):
            if all(not set(favoriteCompanies[i]).issubset(favoriteCompanies[j]) for j in range(len(favoriteCompanies)) if i!=j): ans.append(i)
            i += 1
       
        return ans
