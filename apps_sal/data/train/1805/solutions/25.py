class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque([id])
        visited = set()
        visited.add(id)
        for _ in range(level):
            for _ in range(len(q)):
                curr = q.popleft()
                for friend in friends[curr]:
                    if friend not in visited:
                        q.append(friend)
                        visited.add(friend)
        video_dict = defaultdict(int)
        for friend in q:
            for video in watchedVideos[friend]:
                video_dict[video] += 1
        res = [k for (k, v) in sorted(list(video_dict.items()), key=lambda item: (item[1], item[0]))]
        return res

    def fast(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int):
        res = []
        visited = [False] * len(friends)
        fr_set = set()
        q = deque([id])
        for _ in range(level):
            size = len(q)
            for n in range(size):
                fId = q.popleft()
                for f in friends[fId]:
                    if visited[f] != True and f != id:
                        q.append(f)
                        visited[f] = True
        dic = {}
        while q:
            fid = q.popleft()
            for video in watchedVideos[fid]:
                dic[video] = dic.get(video, 0) + 1
        res = [k for (k, v) in sorted(list(dic.items()), key=lambda item: (item[1], item[0]))]
        return res
