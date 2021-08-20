class Solution:

    def peopleIndexes(self, favorites: List[List[str]]) -> List[int]:
        parents = []
        parent_sets = []
        for i in sorted(range(len(favorites)), key=lambda i: len(favorites[i]), reverse=True):
            c = set(favorites[i])
            is_parent = True
            for p in parent_sets:
                if c.issubset(p):
                    is_parent = False
                    break
            if is_parent:
                parents.append(i)
                parent_sets.append(c)
        return sorted(parents)
