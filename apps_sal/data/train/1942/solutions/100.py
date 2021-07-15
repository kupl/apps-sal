class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = [x for x in range(len(favoriteCompanies))]
        for i in range(len(favoriteCompanies)):
            for j in range(i+1,len(favoriteCompanies)):
                set1 = set(favoriteCompanies[i])
                set2 = set(favoriteCompanies[j])
                if set1.issubset(set2):
                    ans[i] = -1
                elif set2.issubset(set1):
                    ans[j] = -1
        return [x for x in ans if x >=0]
