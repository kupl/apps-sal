class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d={}
        for ind,company in enumerate(favoriteCompanies):
            for e in company:
                if e not in d:
                    d[e]=set()
                d[e].add(ind)
        #print('d',d)
        output=[]
        for ind,company in enumerate(favoriteCompanies):
            temp=d[company[0]]
            for e in company[1:]:
                temp=temp.intersection(d[e])
            if len(temp)<=1:
                output.append(ind)
        return output
            

