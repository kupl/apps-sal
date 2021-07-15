class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        #15
        mp = {}
        num_person = len(favoriteCompanies)
        for i in range(num_person):
            p = favoriteCompanies[i]
            for v in p:
                if v not in mp:
                    mp[v] = set()
                mp[v].add(i)
        result = []
        for i in range(num_person):
            p = favoriteCompanies[i]
            common = {}
            found = False
            for v in p:
                for k in mp[v]:
                    if k not in common:
                        common[k] = 0
                    common[k] += 1
                    if common[k] == len(p) and k != i:
                        found = True
                        break
                if found == True:
                    break
            if found == False:
                result.append(i)
        return result
