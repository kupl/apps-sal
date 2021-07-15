from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        # BFS search
        persons = len(friends)
        visited = [False]*persons
        source = id
        visited[source] = True
        
        queue = deque()
        queue.append(source)
        k = 0
        
        videos_counter = Counter()
        
        while queue and k < level:
            
            videos_counter = Counter()
            q_len = len(queue)
            for _ in range(q_len):
                person = queue.popleft()
                
                # search all the watched videos of your friend
                for friend in friends[person]:
                    if visited[friend]:
                        continue
                    
                    visited[friend] = True
                    queue.append(friend)
                    videos = watchedVideos[friend]
                    # update the videos_counter
                    for video in videos:
                        videos_counter[video] += 1

            
            k += 1  # update the level
        
        # collect the videos with their frequencies
        frequencies = [(frequency, video) for video, frequency in list(videos_counter.items())]
        
        # sort them in increasing order with respect to frequency
        result = [video for freq, video in sorted(frequencies)]
        return result

