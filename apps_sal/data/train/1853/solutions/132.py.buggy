class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        
        city=0
        value=float(\"inf\")
        graph=defaultdict(list)
        for i,j,c in edges:
            graph[i].append([j,c])
            graph[j].append([i,c])
        
        def heap(start):
            visited=set()
            minheap=[(0,start)]
            while minheap:
                cost,node=heapq.heappop(minheap)
                if cost<=distanceThreshold:
                    visited.add(node)
                else:
                    continue
                for i,j in graph[node]:
                    if i not in visited:
                        heapq.heappush(minheap,(j+cost,i))
            return len(visited)-1
        for i in range(n):
            ans=heap(i)
            if ans<=value:
                value=ans
                city=i
        return city
        
