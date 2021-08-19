class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        stack = [(0, id)]
        visited = set([id])
        friendsSet = set()
        while stack:
            (lNow, fi) = heapq.heappop(stack)
            if lNow == level:
                friendsSet.add(fi)
            else:
                for fi1 in friends[fi]:
                    if fi1 not in visited:
                        visited.add(fi1)
                        heapq.heappush(stack, (lNow + 1, fi1))
        videoCounter = Counter()
        for f in friendsSet:
            videoCounter += Counter(watchedVideos[f])
        ans = sorted([key for key in videoCounter], key=lambda x: (videoCounter[x], x))
        return ans
