class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        graph = defaultdict(list)
        
        #build graph
        for i, v in enumerate(friends):
            graph[i].extend(v)
            for r in v:
                graph[r].append(i)
        
        
        
        videos = defaultdict(int)
        def bfs(source):
            dq = deque([source])
            visited = set()
            visited.add(source)
            nlevels = 0
            
            while dq:
                for _ in range(len(dq)):
                    node = dq.popleft()
                    if nlevels == level:
                        for v in watchedVideos[node]:
                            videos[v] += 1
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            dq.append(nei)
                    
                nlevels += 1
        bfs(id)            
        minheap = []
        for v in sorted(videos.keys()):
            heappush(minheap, (videos[v], v)) 

        res = []
        while minheap:
            res.append(heappop(minheap)[1])
        return res
        

