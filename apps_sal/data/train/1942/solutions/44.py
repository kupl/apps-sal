class Solution:
    def _subset(self, fav, result):
        for x in result:
            if not fav - x:
                return True
        return False

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favorite_companies = [tuple(sorted(x)) for x in favoriteCompanies]
        val_to_key = {x: i for i, x in enumerate(favorite_companies)}
        len_to_comp = collections.defaultdict(list)
        for x in favorite_companies:
            len_to_comp[len(x)].append(set(x))
        sorted_keys = sorted(len_to_comp, reverse=True)
        result = []
        for key in sorted_keys:
            curr = []
            for fav in len_to_comp[key]:
                if not self._subset(fav, result):
                    curr.append(fav)
            result += curr
        result = [tuple(sorted(x)) for x in result]
        return sorted([val_to_key[x] for x in result])
