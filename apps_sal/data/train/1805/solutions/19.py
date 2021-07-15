class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    
        q = deque([id])
        visited = set()
        visited.add(id)
        
        # q contains friends at level k
        for _ in range(level):
            for _ in range(len(q)):
                curr = q.popleft()
                for friend in friends[curr]:
                    if friend not in visited:
                        q.append(friend)
                        visited.add(friend)
                        
        
        # get videos for friends at level k
        video_dict = {}
        for friend in q:
            for video in watchedVideos[friend]:
                video_dict[video] = video_dict.get(video, 0) + 1
              
        res = [k for k, v in sorted(video_dict.items(), key=lambda item: (item[1],item[0]))]
        
        return res
