class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph,n,temp,edge=collections.defaultdict(list),len(points),float(\"inf\"),[-1,-1]
        for i in range(n):
            for j in range(i+1,n):
                x,y,a,b=points[i][0],points[i][1],points[j][0],points[j][1]
                dist=abs(x-a)+abs(y-b)
                graph[i].append((dist,j))
                graph[j].append((dist,i))
                if dist<temp:
                    temp=dist
                    edge=[i,j]
        ans,vis,queue,vis_count=0,{0},graph[0],1
        heap=heapq.heapify(queue)
        while queue and vis_count<n:
            d,v=heapq.heappop(queue)
            if v in vis: continue
            ans+=d
            vis_count+=1
            vis.add(v)
            for connected in graph[v]:
                if connected[1] in vis: continue
                heapq.heappush(queue,connected)
        return ans
