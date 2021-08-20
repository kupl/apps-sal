class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d = {}
        n = len(favoriteCompanies)
        A = []
        for (j, arr) in enumerate(favoriteCompanies):
            A.append((arr, j))
        A.sort(key=lambda x: len(x[0]), reverse=True)
        print(A)
        ans = []
        s1 = set()
        for i in range(n):
            k = A[i][1]
            s1.add(k)
            temp = s1
            for (j, c) in enumerate(A[i][0]):
                if c not in d:
                    d[c] = set([k])
                else:
                    d[c].add(k)
                temp = temp.intersection(d[c])
            if len(temp) == 1:
                ans.append(k)
        ans.sort()
        return ans
