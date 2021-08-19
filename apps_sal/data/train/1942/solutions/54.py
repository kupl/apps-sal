class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # ans = []
        # s = [set(cs) for cs in favoriteCompanies]
        # print(s)
        # for i, s1 in enumerate(s):
        #     if all (i == j or not s1.issubset(s2) for j, s2 in enumerate(s)):
        #         ans.append(i)
        # return ans

        people = []
        sets = [set(a) for a in favoriteCompanies]
        for i, a in enumerate(sets):
            for j, b in enumerate(sets):
                if i == j:
                    continue
                if a.issubset(b):
                    break
            else:
                people.append(i)

        return people
