class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        g_friends = collections.defaultdict(list)
        for i in range(len(friends)):
            for f in friends[i]:
                g_friends[i].append(f)
        queue = collections.deque()
        queue.append((id, 0))
        visited = set([id])
        videos = collections.defaultdict(int)
        while queue:
            size = len(queue)
            for _ in range(size):
                (curr_id, curr_level) = queue.popleft()
                if curr_level == level:
                    for v in watchedVideos[curr_id]:
                        videos[v] += 1
                else:
                    for f in g_friends[curr_id]:
                        if f not in visited:
                            visited.add(f)
                            queue.append((f, curr_level + 1))
        return [v for (_, v) in sorted([(f, v) for (v, f) in list(videos.items())])]
