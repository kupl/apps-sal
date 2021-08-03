from collections import defaultdict, deque


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        adj = [[] for i in range(n)]
        for i in range(n):
            adj[i] = friends[i]
        req = []
        visited = {}
        q = deque()
        q.append((id, 0))
        visited[id] = True
        while q:
            u, lev = q.popleft()
            if lev == level:
                req.append(u)
                continue
            if lev > level:
                break
            for f in adj[u]:
                if f not in visited:
                    q.append((f, lev + 1))
                    visited[f] = True
        res = defaultdict(lambda: 0)
        for f in req:
            for mov in watchedVideos[f]:
                res[mov] += 1
        res = sorted(res.items(), key=lambda x: (x[1], x[0]))
        movies = [i[0] for i in res]
        return movies
