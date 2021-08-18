class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(x, y, d):
            nonlocal res
            count = 0
            arr = []
            for key, val in d.items():
                if x in val and y in val:
                    res += 1
                    count = -1
                    break
                elif x in val or y in val:
                    d[key].add(x)
                    d[key].add(y)
                    count += 1
                    arr.append(key)

            if count == -1:
                pass
            elif count == 0:
                d[min(x, y)] = set({x, y})
            elif count == 1:
                pass
            else:
                d[min(arr)].update(d[max(arr)])
                del d[max(arr)]
            return d

        d = {1: set({1})}
        da = dict()
        db = dict()
        res = 0

        a, b, c = [], [], []
        for t, i, j in edges:
            if t == 3:
                a.append([t, i, j])
            elif t == 2:
                b.append([t, i, j])
            else:
                c.append([t, i, j])

        for t, i, j in a:
            d = find(i, j, d)
        da = d
        db = deepcopy(d)

        for t, i, j in b:
            db = find(i, j, db)

        for t, i, j in c:
            da = find(i, j, da)

        if da[1] == db[1] == set(range(1, n + 1)):
            return res
        else:
            return -1
