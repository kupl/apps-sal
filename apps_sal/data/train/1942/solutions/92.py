\"\"\"

\"\"\"
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(companies) for companies in favoriteCompanies]
        output = [] 
        
        for i in range (len(sets)):
            superset = True
            for j in range(len(sets)):
                if i == j: continue
                if sets[i].issubset(sets[j]):
                    superset = False
                    break
            if superset:
                output.append(i)
                
        return output
