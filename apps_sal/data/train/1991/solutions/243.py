class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        pos_start = locations[start]
        pos_finish = locations[finish]
        locations.sort()
        start = locations.index(pos_start)
        finish = locations.index(pos_finish)
        # print(locations, start, finish)
             
        @lru_cache(maxsize = None)
        def find(start, fuel):
            count = 0
            if abs(start-finish)==1 and fuel==abs(locations[start] - locations[finish]):
                return 1
            if locations[start] == locations[finish]:
                    count += 1
            if fuel >= abs(locations[start] - locations[finish]):
                for i in range(start-1, -1, -1):
                    if abs(locations[start] - locations[i]) + abs(locations[i] - locations[finish]) <= fuel:
                        count += find(i, fuel - abs(locations[start] - locations[i]))
                    else:
                        break
                for j in range(start+1, len(locations)):
                    if abs(locations[start] - locations[j]) + abs(locations[j] - locations[finish]) <= fuel:
                        count += find(j, fuel - abs(locations[start] - locations[j]))
                    else:
                        break
            return count
        return find(start, fuel) % MOD
                        
            
        
        
        
        
#         X X X start X X X finish X X X
        
#         重点不在于city的编号，而在于他们的位置
#         每个位置都有一个fuel的值
#         首先保证
#         用递归算法，第一层从start的位置出发，考察start可以到达的位置以及剩余的fuel
#         第二层从start可以到达的位置出发，继续减少fuel并考虑相应的次数
#         后面继续迭代，直到只能直接到达的城市
#         find(pos, fuel) 返回路径数量
#         res = find(start, fuel)
        

