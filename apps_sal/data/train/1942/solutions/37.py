class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        a = [set(y) for y in favoriteCompanies]

        def check(i):
            return all([i == j or not a[i].issubset(a[j]) for j in range(len(a))])
        return [i for i in range(len(a)) if check(i)]
