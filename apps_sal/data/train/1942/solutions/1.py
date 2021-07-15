class Person:
    def __init__(self, index, favoriteCompanies):
        self.index = index
        self.favoriteCompanies = set(favoriteCompanies)
        self.size = len(favoriteCompanies)
    
    def __repr__(self):
        return \"{}\".format(self.favoriteCompanies)

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        people = [Person(i, l) for i, l in enumerate(favoriteCompanies)]
        people.sort(key = lambda person : person.size, reverse = True)
        
        res = []
        for i in range(len(people)):
            contained = False
            for j in range(i):
                if people[i].favoriteCompanies.issubset(people[j].favoriteCompanies):
                    contained = True
                    break
            if not contained:
                res.append(people[i].index)
        
        return sorted(res)
