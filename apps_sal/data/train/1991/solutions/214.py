class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def cost(i, j): return abs(locations[i] - locations[j])

        @lru_cache(None)
        def dfs(i, f):
            if f < 0:
                return 0
            return sum([dfs(j, f - cost(i, j)) for j in range(len(locations)) if j != i]) + (i == finish)
        return dfs(start, fuel) % (10**9 + 7)

# [1528,1529,1530,1531,1532,1533,1534,1535,1536,1538,1539,1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621,1622,1623,1624,1625,1626,1627,1628]
# 50
# 50
# 200

#         self.rout_dict = {}
#         start_val, end_val = min(locations[start], locations[finish]), max(locations[start], locations[finish])

#         if end_val-start_val > fuel:
#             return 0

#         def subRoutes(loc, start, end, fuel):
#             if (loc[start], loc[end], fuel) in self.rout_dict:
#                 return self.rout_dict[(loc[start], loc[end], fuel)]
#             elif loc[end] - loc[start] == fuel:
#                 self.rout_dict[(loc[start], loc[end], fuel)] = 2**(end-start-1)
#                 return 2**(end-start-1)
#             elif len(loc) == 1:
#                 return 1
#             else:
#                 # scan possible interval
#                 l_bound, r_bound = -1, len(loc)
#                 for i in range(len(loc)):
#                     if loc[start]+loc[end]-2*loc[i]> fuel:
#                         l_bound = max(i, l_bound)
#                     if loc[start]+loc[end]-2*loc[i]<-fuel:
#                         r_bound = min(i, r_bound)

#                 l_bound += 1
#                 next_loc = loc[l_bound:r_bound]
#                 result = start==end
#                 for i in range(len(next_loc)):
#                     if not i == start-l_bound:
#                         if i > end-l_bound:
#                             result += subRoutes(next_loc, end-l_bound, i, fuel-abs(next_loc[i]-next_loc[start-l_bound]))
#                         else:
#                             result += subRoutes(next_loc, i, end-l_bound, fuel-abs(next_loc[i]-next_loc[start-l_bound]))

#                 self.rout_dict[(loc[start], loc[end], fuel)] = result
#                 return result


#         loc = sorted(locations)
#         for i in range(len(loc)):
#             if loc[i] == start_val:
#                 start_i = i
#             if loc[i] == end_val:
#                 end_i = i
#                 break

#         result=subRoutes(loc, start_i, end_i, fuel)
#         return result%(10**9+7)
