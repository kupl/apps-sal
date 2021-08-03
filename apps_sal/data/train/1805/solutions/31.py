class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        a, d, w = [id], [1] * n, {}
        d[id] = 0
        for _ in range(level):
            b = []
            for i in a:
                for j in friends[i]:
                    if d[j]:
                        b.append(j)
                        d[j] = 0
            a = b
        for i in a:
            for x in watchedVideos[i]:
                w[x] = w.get(x, 0) + 1
        return sorted(w.keys(), key=lambda x: (w[x], x))
