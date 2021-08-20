class Solution:

    def peopleIndexes(self, fav: List[List[str]]) -> List[int]:
        l = []
        l1 = []
        for i in range(len(fav)):
            for j in range(len(fav)):
                if j is not i and set(fav[i]).issubset(set(fav[j])):
                    l.append(i)
        for i in range(len(fav)):
            if i not in l:
                l1.append(i)
        return l1
