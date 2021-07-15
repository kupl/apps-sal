class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = collections.defaultdict(dict)
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                d = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                dist[i][j] = dist[j][i] = d
        # print(dist)
        ret = 0
        visited = set([])
        pq = [(0,0)] # dist to s, index, dist to neighbour
        while pq:
            cnt,ind = heapq.heappop(pq)
            if ind not in visited:
                ret += cnt
                visited.add(ind)
                # print(ret,pq)
                for nei in dist[ind]:
                    if nei not in visited:
                        heapq.heappush(pq,(dist[ind][nei],nei))
        return ret
                
                

