class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cache = []
        l = len(points)
        if l == 1:
            return 0

        for i in range(l-1):
            for j in range(i+1, l):
                start = points[i]
                end = points[j]
                length = abs(start[0]-end[0])+abs(start[1]-end[1])
                cache.append([length, i, j])
        cache.sort()
        #print(cache)

        res = 0
        t = len(cache)
        count = 0
        group = []
        for i in range(t):
            #print(group)
            
            curr = cache[i]
            g = len(group)
            a = None
            b = None
            for j in range(g):
                if curr[1] in group[j]:
                    a = j
                if curr[2] in group[j]:
                    b = j
            #print(a,b)

            if a == None and b == None:
                group.append({curr[1], curr[2]})
            elif a == None:
                group[b].add(curr[1])
            elif b == None:
                group[a].add(curr[2])
            else:
                if a == b:
                    continue
                else:
                    group[a] = group[a] | group[b]
                    group.pop(b)
            count += 1
            res += curr[0]   
            if count == l-1:
                #print(group)
                return res

