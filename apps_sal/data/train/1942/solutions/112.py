class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        N = len(favoriteCompanies)
        result = list(range(0,N))
        
        for i in range(0,N):
            a = set(favoriteCompanies[i])
            for j in range(0,N):
                if i == j or len(a) > len(favoriteCompanies[j]):
                    continue
                    
                b = set(favoriteCompanies[j])
                if a.intersection(b) == a:
                    result.remove(i)
                    break
                    
        return result

