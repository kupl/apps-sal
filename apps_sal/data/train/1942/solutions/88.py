class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        f_C = []
        for company in favoriteCompanies:
            f_C.append(set(company))
        print(f_C)
        n = len(f_C)
        ans = []
        for i in range(n):
            flag = 1
            for j in range(n):
                if i == j:
                    continue
                if f_C[i] & f_C[j] == f_C[i]:
                    flag = 0
                    break
            if flag == 1:
                ans.append(i)
        return ans
