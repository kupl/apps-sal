class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        frontier = [id]
        seen = {id}
        depth = 0
        while frontier:
            next_frontier = []
            if depth == level - 1:
                count = collections.defaultdict(lambda: 0)
            for p in frontier:
                for fr in friends[p]:
                    if fr not in seen:
                        seen.add(fr)
                        if depth == level - 1:
                            for video in watchedVideos[fr]:
                                count[video] += 1
                        next_frontier.append(fr)
            frontier = next_frontier
            depth += 1
            if depth == level:
                return sorted(count.keys(), key=lambda x: [count[x], x])

        return []
