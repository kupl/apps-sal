class Solution:
    def peopleIndexes(self, favorites: List[List[str]]) -> List[int]:
        # res = []
        # l = len(favoriteCompanies)
        # for i in range(l):
        #     f = 0
        #     for j in range(l):
        #         if i != j:
        #             if set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])):
        #                 f=1
        #                 break
        #     if f==0:
        #         res.append(i)
        # return res
        
        parents = []
        parent_sets = []
        for i in sorted(range(len(favorites)), key=lambda i: len(favorites[i]), reverse=True):
            c = set(favorites[i])
            
            is_parent = True
            for p in parent_sets:
                if c.issubset(p):
                    is_parent = False
                    break
            
            if is_parent:
                parents.append(i)
                parent_sets.append(c)
            
        return sorted(parents)
