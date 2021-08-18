class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        m = len(queries)
        d = {}
        res = []
        d['0 0'] = arr[0]
        for i in range(1, n):
            key = '{} {}'.format(0, i)
            pkey = '{} {}'.format(0, i - 1)
            d[key] = d[pkey] ^ arr[i]
        print(d)
        for i in range(0, m):
            (u, v) = queries[i]
            s = 0
            key2 = '{u} {v}'.format(u=u, v=v)
            if key2 in d:
                res.append(d[key2])
                continue

            pkey = '{} {}'.format(0, u - 1)
            key = '{} {}'.format(0, v)
            s = d[pkey] ^ d[key]
            print(d[pkey], d[key], s)
            res.append(s)
        return res
