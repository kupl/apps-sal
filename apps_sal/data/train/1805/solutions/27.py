class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        friend_dist = [math.inf] * n
        
        friend_dist[id] = 0
        deque = collections.deque()
        deque.append(id)
        
        watched = dict()
        
        while deque:
            person = deque.popleft()
            
            if friend_dist[person] == level:
                for video in watchedVideos[person]:
                    watched[video] = watched.get(video,0) +1
                continue

            for friend in friends[person]:
                if friend_dist[friend] == math.inf:
                    friend_dist[friend] = friend_dist[person] + 1
                    deque.append(friend)
        
        return sorted(watched.keys(), key=lambda v: (watched[v],v))
