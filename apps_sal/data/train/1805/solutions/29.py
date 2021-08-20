class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], ID: int, level: int) -> List[str]:
        freqs = dict()
        visited = set()
        visited.add(ID)
        q = set()
        q.add(ID)
        for _ in range(level):
            q = {j for i in q for j in friends[i] if j not in visited}
            visited |= q
        for p in q:
            for v in watchedVideos[p]:
                freqs[v] = freqs.get(v, 0) + 1
        sortedfreqs = sorted([(n, v) for (v, n) in list(freqs.items())])
        return [v for (_, v) in sortedfreqs]
