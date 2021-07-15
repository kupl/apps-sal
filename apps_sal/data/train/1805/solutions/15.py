from collections import defaultdict


class Movie:
    def __init__(self, name):
        self.name = name
        self.freq = 0
    
    def __lt__(self, other):
        if not other:
            return True
        if self.freq != other.freq:
            return self.freq < other.freq
        
        return self.name < other.name

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        if not watchedVideos or not friends or level == 0:
            return []
        
        
        movies_freq = {}
        queue = deque()
        queue.append(id)
        cur_level = 0
        visited = set()
        visited.add(id)
        while queue:
            n = len(queue)
            if cur_level == level:
                break
            cur_level += 1
            for _ in range(n):
                node = queue.popleft()
                if node >= len(friends):
                    continue
                
                for child in friends[node]:
                    if child in visited:
                        continue
                    visited.add(child)
                    queue.append(child)

        while queue:
            friend = queue.popleft()
            if friend >= len(watchedVideos):
                continue
            
            for video in watchedVideos[friend]:
                if video not in movies_freq:
                    video_obj = Movie(video)
                    movies_freq[video] = video_obj
                movies_freq[video].freq += 1
        
        if not movies_freq:
            return []
        
        *result, = [x.name for x in sorted(movies_freq.values())]
        return result

