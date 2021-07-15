class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d={i: set(v) for i,v in enumerate(favoriteCompanies) }
        ans=[]
        n=len(favoriteCompanies)
        for i in range(n):
            subSet=True
            for j in range(n):
                if i==j:
                    continue
                if not d[i]-d[j]:
                    subSet=False
                    break
            if subSet:
                ans.append(i)
        return ans

