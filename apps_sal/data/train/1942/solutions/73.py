class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # s=set()
        # b=set()
        # x=s.intersection(b)
        glb = set()
        ct = 0
        # d={}
        ds = {}
        for i in favoriteCompanies:
            for j in i:
                if j not in glb:
                    ct = ct + 1
                    ds[j] = ct
                    glb.add(j)
        d = collections.defaultdict(set)

        for i in range(len(favoriteCompanies)):
            new = set()
            for j in favoriteCompanies[i]:
                new.add(ds[j])

            d[i] = new
        ar = []
        for i in range(len(favoriteCompanies)):
            found = 0
            for j in range(len(favoriteCompanies)):
                if i != j:
                    x = d[i].intersection(d[j])
                    if x == d[i]:
                        found = 1
                        break
            if found == 0:
                ar.append(i)

        return ar
