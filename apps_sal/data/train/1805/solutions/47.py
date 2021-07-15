class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = collections.defaultdict(set)
        
        for i in range(len(friends)):
            for friend in friends[i]:
                graph[i].add(friend)
                graph[friend].add(i)
        
        levelOfFriends = [id]
        visited = set([id])
        l = 0

        while levelOfFriends and l < level:
            size = len(levelOfFriends)
            l += 1
            
            for _ in range(size):
                f = levelOfFriends.pop(0)
                
                for otherF in graph[f]:
                    if otherF not in visited:
                        levelOfFriends.append(otherF)
                        visited.add(otherF)
                    
        w = collections.defaultdict(int)
        
        for f in levelOfFriends:
            videos = watchedVideos[f]
            
            for v in videos:
                w[v] += 1
                
        heap = []
        
        for v in list(w.keys()):
            heapq.heappush(heap, (w[v], v))
            
        res = []
        for _ in range(len(heap)):
            _, v = heapq.heappop(heap)
            res.append(v)
            
        return res
                

