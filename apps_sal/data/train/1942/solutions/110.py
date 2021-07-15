class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # make companies -> person dict
        # for each person, find if the don't have a subset
        ans = []
        favorites = defaultdict(list)
        for i, person in enumerate(favoriteCompanies):
            for company in person:
                favorites[company].append(i)
        
        for i, person in enumerate(favoriteCompanies):
            possible_supersets = set(range(len(favoriteCompanies)))
            possible_supersets.remove(i)
            for companies in person:
                possible_supersets = possible_supersets.intersection(set(favorites[companies]))
                if len(possible_supersets) == 0:
                    break
            if len(possible_supersets) == 0:
                ans.append(i)
        return ans
