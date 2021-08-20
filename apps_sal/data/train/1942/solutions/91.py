class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        from collections import Counter
        words = {}
        subsets = []
        for (i, x) in enumerate(favoriteCompanies):
            for y in x:
                if y not in words:
                    words[y] = [i]
                else:
                    words[y].append(i)
        for (i, x) in enumerate(favoriteCompanies):
            c = Counter()
            for y in x:
                c.update(words[y])
            for item in c.most_common():
                if item[0] != i:
                    if item[1] >= len(x):
                        break
                    else:
                        subsets.append(i)
                        break
                elif len(c) == 1:
                    subsets.append(i)
        return subsets
