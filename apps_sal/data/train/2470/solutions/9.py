from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # ans = 0
        # dominoes = sorted([sorted(i) for i in dominoes])
        # # print(dominoes)
        # prev = dominoes.pop()
        # cnt = 0
        # tot = 0
        # while dominoes:
        #     curr = dominoes.pop()
        #     # print('curr ', curr)
        #     if curr == prev:
        #         cnt += 1
        #         tot += cnt
        #     else:
        #         ans += tot
        #         tot, cnt = 0, 0
        #     prev = curr
        # return ans + tot
                
        
        # step 1: count the dominoes
        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        c = 0
        for n in list(d.values()):
            s = n*(n-1)//2
            c += s
        return c

