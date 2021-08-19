from collections import defaultdict


class Solution:
    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        li = [[int(t[0:2]) * 100 + int(t[3:]), n] for t, n in zip(time, name)]
        li = sorted(li)
        d = defaultdict(int)
        dc = defaultdict(int)
        n = len(name)
#         s= set()
#         print(li)
#         for i in range(n):
#             if li[i][1] in d:
#                 print(d[li[i][1]] ,li[i][0],-d[li[i][1]] +li[i][0])
#                 if  li[i][0] -d[li[i][1]] <=100:
#                     pass

#                 else:
#                     dc[li[i][1]] =0

#             d[li[i][1]]= li[i][0]

#             dc[li[i][1]]+=1
#             if dc[li[i][1]]>=3:
#                 s.add(li[i][1])
#             print(dc,d)

        i, j = 0, 0
        ans = 0
        # print(li)
        s = set()
        while i <= j and j < n:
            #print(li[j][0]-li[i][0], i,j)
            if li[j][0] - li[i][0] == 0:
                d[li[j][1]] = 1
                j += 1
            elif li[j][0] - li[i][0] <= 100:
                d[li[j][1]] += 1
                # print(d[li[j][1]],\"sg\")
                if d[li[j][1]] >= 3:
                    s.add(li[j][1])
                j += 1

            else:

                d[li[i][1]] -= 1
                i += 1
        return sorted(list(s))
