class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:    
        
        order = {tuple(value):idx for idx, value in enumerate(favoriteCompanies)}
        favoriteCompanies  = sorted(favoriteCompanies,key=len,reverse=True)
        ans = []
        visited = []
        for fav in favoriteCompanies:
            
            find = 0
            for v in visited: 
                if set(v) & set(fav) == set(fav):
                    find = 1
                    break
            if find == 0:
                visited.append(fav)
                ans.append(order[tuple(fav)])
        
            
        return sorted(ans)
