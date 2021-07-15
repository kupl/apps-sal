from heapq import heappush, heappop
class Solution(object):
    def rectangleArea(self, recs):
        \"\"\"
        :type rectangles: List[List[int]]
        :rtype: int
        \"\"\"
        x = set()
        pq = []
        for rec in recs:
            x.add(rec[0])
            x.add(rec[2])
            heappush(pq, (rec[1], rec[0], rec[2], 1))
            heappush(pq, (rec[3], rec[0], rec[2], -1))
        
        x = sorted(list(x))
        xi = {v:i for i,v in enumerate(x)}
        count = [0] * len(x)
        
        res = 0
        last_l = cur_l = pq[0][0]
        
#         print(pq)
        
        while pq:
#             print(pq)
#             print(count)
            cur_l = pq[0][0]

            for i in range(len(x)):
                if count[i] > 0:
                    res += (x[i+1] - x[i]) * (cur_l-last_l)
                    res = res % (10**9 + 7)
            while pq and pq[0][0] == cur_l:
#                 print(cur_l, pq)
                cur_l, x1, x2, bound = heappop(pq)
                for i in range(xi[x1],xi[x2]):
                    count[i] += bound
            
            last_l = cur_l
        return res
