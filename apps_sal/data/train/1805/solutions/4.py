class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        bfs, visited = {id}, {id}
        for _ in range(level):
            bfs = {j for i in bfs for j in friends[i] if j not in visited}
            visited |= bfs
        freq = collections.Counter([v for idx in bfs for v in watchedVideos[idx]])
        return sorted(list(freq.keys()), key=lambda x: (freq[x], x))
