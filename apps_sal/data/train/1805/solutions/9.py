from collections import defaultdict
import heapq


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # (count, c)
        adj = {}
        for i in range(len(friends)):
            adj[i] = friends[i]

        queue = [id]
        visited = set()
        visited.add(id)
        dis = 0
        while queue:
            if dis == level:
                break
            for _ in range(len(queue)):
                cur = queue.pop(0)
                for friend in adj[cur]:
                    if friend not in visited:
                        queue.append(friend)
                        visited.add(friend)
            dis += 1
        count = defaultdict(int)
        for people in queue:
            for video in watchedVideos[people]:
                count[video] += 1
        heap = []
        for key in count:
            heapq.heappush(heap, (count[key], key))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
