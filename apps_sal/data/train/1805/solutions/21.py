class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        visited = [False] * n
        que = collections.deque([id])
        visited[id] = True
        cur = 0
        while que and cur < level:
            size = len(que)
            cur += 1
            for _ in range(size):
                node = que.popleft()
                for f in friends[node]:
                    if not visited[f]:
                        visited[f] = True
                        que.append(f)
        cnt = collections.Counter()
        for node in que:
            for m in watchedVideos[node]:
                cnt[m] += 1
        videos = list(cnt.keys())
        videos.sort(key=lambda x: [cnt[x], x])
        return videos
