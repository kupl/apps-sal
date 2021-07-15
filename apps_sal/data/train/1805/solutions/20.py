class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # BFS to find the k-related friends
        visited = {id: 1}
        queue = deque()
        queue.append((id, 0))
        result = []
        while queue:
            u, dist = queue.popleft()
            if dist == level:
                result.append(u)
                continue
            
            for v in friends[u]:
                if v in visited:
                    continue
                visited[v] = 1
                queue.append((v, dist + 1))
                
        # collect the movies
        counter = {}
        for u in result:
            for video in watchedVideos[u]:
                counter[video] = counter.get(video, 0) + 1
                
        # sort the movies
        result = sorted([(times, videos) for videos, times in list(counter.items())])
        return [val[1] for val in result]
        

