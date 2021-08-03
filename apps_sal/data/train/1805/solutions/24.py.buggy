\"\"\"


\"\"\"


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        visited = [0] * n
        visited[id] = 1
        queue = collections.deque()
        queue.append(id)
        persons = []
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                node = queue.popleft()
                for nei in friends[node]:
                    if visited[nei] == 1:
                        continue
                    visited[nei] = 1
                    queue.append(nei)
                    if step == level:
                        persons.append(nei)
            if step == level:
                break
        
        VideoSet = set()
        freq = collections.defaultdict(int)
        for person in persons:
            for v in watchedVideos[person]:
                VideoSet.add(v)
                freq[v] += 1        
        
        temp = []
        for v in VideoSet:
            temp.append([freq[v], v])
        
        temp.sort()
        
        res = []
        for x in temp:
            res.append(x[1])
        return res
        
        
        
        
        
        
        
        
