from heapq import heappush,heappop
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
         d=collections.defaultdict(list);last=[]
         for idx,lake in enumerate(rains):
              d[lake].append(idx)
         ans=[]
         for idx,lake in enumerate(rains):
             if lake:
                if last and last[0]==idx:
                    return []
                arr=d[lake]
                arr.pop(0)
                if arr:
                    heappush(last,arr[0])
                ans.append(-1)
             else:
                 if last:
                    ans.append(rains[heappop(last)])
                 else:
                    ans.append(1)
         return ans
