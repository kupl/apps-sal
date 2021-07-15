class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        name_to_index = {}

        company_indices = []
        for _ in favoriteCompanies:
            indices = []
            for name in _:
                if name not in name_to_index:
                    name_to_index[name] = len(name_to_index)
                indices.append(name_to_index[name])
            print(indices)
            company_indices.append(set(indices))
        print(\"-\" * 10)

        ret = []
        for ix, x in enumerate(company_indices):
            valid = True
            for iy, y in enumerate(company_indices):
                if ix == iy:
                    continue
                if x.union(y) == y:
                    valid = False
                    break
            if valid:
                ret.append(ix)
        return ret

