class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        def judge(i):
            for j in range(n):
                if i != j:
                    contain = True
                    for x in favoriteCompanies[i]:
                        if x not in favoriteCompanies[j]:
                            contain = False
                            break
                    if contain:
                        return False
            return True
        
        n = len(favoriteCompanies)
        favoriteCompanies = list(map(set,favoriteCompanies))
        res = []
        for i in range(n):
            if judge(i): res.append(i)
        return res
                            

