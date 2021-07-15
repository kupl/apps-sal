from collections import defaultdict
class Solution:
    def minAreaRect(self, points):
        X = list(zip(*points))
        if len(set(X[0])) == 1 or len(set(X[1])) == 1: return 0

        points.sort()
        columns = defaultdict(list)
        for r, c in points:
            columns[r].append(c)
        ans, lastc = float('inf'), dict()
        for r, cols in list(columns.items()):
            for i, c1 in enumerate(cols):
                for c2 in cols[i+1:]:
                    if (c1, c2) in lastc:
                        area = (r - lastc[(c1, c2)]) * (c2 - c1)
                        #ans = min(ans, area)
                        if area < ans: ans = area
                    lastc[(c1, c2)] = r
        return ans if ans < float('inf') else 0

# from collections import defaultdict
# class Solution:
#     def minAreaRect(self, points):
#         d = defaultdict(set)
#         rset, cset, N, ans = set(), set(), len(points), float('inf')
#         for r, c in points:
#             rset.add(r)
#             cset.add(c)
#         Nr, Nc = len(rset), len(cset)
#         if Nr == N or Nc == N:
#             return 0
#         elif Nr < Nc:
#             for r, c in points:
#                 d[r].add(c)
#         else:
#             for r, c in points:
#                 d[c].add(r)
# 
#         A = sorted(d.keys())
#         for i, r1 in enumerate(A):
#             cols1 = d[r1]
#             for r2 in A[i+1:]:
#                 cols2 = d[r2]
#                 s = sorted(cols1 & cols2)
#                 for c1, c2 in zip(s[:-1], s[1:]):
#                     area = abs((r1 - r2) * (c1 - c2))
#                     ans = min(ans, area)
#         return ans if ans < float('inf') else 0

