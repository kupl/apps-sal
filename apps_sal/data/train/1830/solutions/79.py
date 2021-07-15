# from bisect import bisect_left

# class Solution:
#     def avoidFlood(self, rains: List[int]) -> List[int]:
#         flooded = {}
#         dry_days = []
#         out = [-1 for _ in range(len(rains))]
        
#         for i in range(len(rains)):
#             day = rains[i]
#             if day > 0:
#                 if day in flooded:
#                     if dry_days:
#                         # found = False
#                         # for d in range(len(dry_days)):
#                         #     dry_day = dry_days[d]
#                         #     if dry_day > flooded[day]:
#                         #         out[dry_day] = day
#                         #         dry_days.pop(d)
#                         #         found = True
#                         #         break
#                         # if not found:
#                         #     return []
#                         dry = bisect_left(dry_days, flooded[day])
#                         if dry == len(dry_days):
#                             return []
#                         else:
#                             dry_day = dry_days.pop(dry)
#                             out[dry_day] = day
#                     else:
#                         return []
#                 flooded[day] = i
#             else:
#                 dry_days.append(i)
#         for dry_day in dry_days:
#             out[dry_day] = 1
#         return out

from sortedcontainers import SortedList as sl
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1]*(len(rains))
        has_rained = dict()
        free = sl()
        for i in range(len(rains)):
            # print(free)
            if rains[i]==0:
                free.add(i)
            else:
                if rains[i] not in has_rained:
                    has_rained[rains[i]]=i
                else:
\t\t\t\t\t# no free days are available
                    if len(free)==0:
                        return []
\t\t\t\t\t#finding the index of the free day that came after the first occurance of
\t\t\t\t\t# rains[i]
                    idx = free.bisect_left(has_rained[rains[i]])
                    # print(free,idx,i,has_rained)
                    if idx<len(free):
                        ans[free[idx]]=rains[i]
\t\t\t\t\t\t# updating the index of rains[i] for future it's future occurances
                        has_rained[rains[i]] = i
                        free.remove(free[idx])
                    else:
\t\t\t\t\t\t#if no such index exists then return
                        return []
        if len(free):
            while free:
\t\t\t\t# choosing some day to dry on the remaining days
                ans[free.pop()]=1
        return ans
