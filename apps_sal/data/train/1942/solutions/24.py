class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        result = []
        for i in range(len(favoriteCompanies)):
            f = True
            for x in favoriteCompanies[:i] + favoriteCompanies[i + 1:]:
                if set(favoriteCompanies[i]).intersection(set(x)) == set(favoriteCompanies[i]):
                    f = False
                    break
            if f:
                result.append(i)
        return result
