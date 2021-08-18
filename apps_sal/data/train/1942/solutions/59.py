class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        name2idx = {}
        group = {}

        for i in range(len(favoriteCompanies)):
            for item in favoriteCompanies[i]:
                if not item in name2idx:
                    name2idx[item] = len(name2idx)

        for i in range(len(favoriteCompanies)):
            favoriteCompanies[i] = [name2idx[x] for x in favoriteCompanies[i]]

        for i in range(len(favoriteCompanies)):
            group[tuple([x for x in favoriteCompanies[i]])] = i

        favoriteCompanies = sorted(favoriteCompanies, key=lambda x: len(x), reverse=True)

        ans = []
        for i in range(len(favoriteCompanies)):
            if len(ans) == 0:
                ans.append(group[tuple([x for x in favoriteCompanies[i]])])
                continue

            cur_set = set(favoriteCompanies[i])
            flag = True
            for j in range(i):
                pre_set = set(favoriteCompanies[j])

                if cur_set.issubset(pre_set):
                    flag = False
                    break

            if flag:
                ans.append(group[tuple([x for x in favoriteCompanies[i]])])

        ans.sort()
        return ans
