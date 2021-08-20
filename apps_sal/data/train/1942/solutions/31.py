class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        for u in favoriteCompanies:
            u.sort()
        L = len(favoriteCompanies)
        dic = {}

        def check(i, j):
            if (i, j) in dic:
                return dic[i, j]
            else:
                stack1 = favoriteCompanies[i].copy()
                stack2 = favoriteCompanies[j].copy()
                while stack1 and stack2:
                    if stack2[0] != stack1[0]:
                        stack2.pop(0)
                    elif stack2[0] == stack1[0]:
                        stack1.pop(0)
                        stack2.pop(0)
                if not stack1:
                    dic[i, j] = True
                    return True
                else:
                    dic[i, j] = False
                    return False
        ans = []
        for i in range(L):
            status = 0
            for j in range(L):
                if j != i and check(i, j):
                    status = 1
                    break
            if status == 0:
                ans.append(i)
        return ans
