class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def method1():
            graph=collections.defaultdict(list)
            for s,d,w in edges:
                graph[s].append((d,w))
                graph[d].append((s,w))
                
            
            def dijkstrase(s):
                queue=[(0,s)]
                seen={s:0}
                
                while queue:
                    w,s=heapq.heappop(queue)
                    for nei,dw in graph[s]:
                        if nei not in seen or w+dw<seen[nei]:
                            seen[nei]=w+dw
                            heapq.heappush(queue, (w+dw,nei))
                
                return seen
            
            distances=[dijkstrase(i) for i in range(n)]
            ans=[]
            for i in range(n):
                total=0
                for k,v in list(distances[i].items()):
                    if 0<v<=distanceThreshold:
                        total+=1
                ans.append(total)
                
            ans=[sum(0<v<=distanceThreshold for k,v in list(distances[i].items())) for i in range(n)]
            return max([i for i in range(n) if ans[i]==min(ans)])
            
        return method1()
            
            
                    
                

