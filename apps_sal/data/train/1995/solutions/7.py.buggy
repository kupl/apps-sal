\"\"\"
[[2,1,5],[3,5,7]]
3 return T

[[3,2,8],[4,4,6],[10,8,9]]
11 return T

[[2,1,5],[3,3,7]]
4 return F

[[4, 1, 3], [8, 2, 3], [1, 3, 6], [8, 4, 6], [4, 4, 8]]
12 return F
\"\"\"
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips: return True
        curr_capacity = capacity
        trips.sort(key=lambda x: (x[1], x[2]))
        print(trips)
        d = collections.defaultdict(list)
        for i, (c, s, e) in enumerate(trips):
            # print(i, c, s, e, d, curr_capacity)
            # if e in d or s in d:
            indexes = []
            # for loc, end_locs in list(d.items():
            for loc in list(d):
                if loc <= s:
                    indexes.extend(d[loc])
                    del d[loc]
                    # indexes = d[s] + d[e]
                    # indexes = d[e]
                    # indexes.extend(d[s])
                    # indexes.ex
                    # print(indexes)
            for index in indexes:
                curr_capacity += trips[index][0]
                    
            curr_capacity -= c
            # print(i)
            if curr_capacity < 0: 
                return False
            d[e].append(i)
            # print(curr_capacity)
        return True
