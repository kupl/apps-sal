from collections import Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        current_level = 0
        nodes_in_current_level = [id]
        visited = set(nodes_in_current_level)
        while current_level < level:
            next_level = []
            while len(nodes_in_current_level) > 0:
                node = nodes_in_current_level.pop()

                for neighbor in friends[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    next_level.append(neighbor)
            nodes_in_current_level = next_level
            current_level += 1
        counter = Counter()
        for id in nodes_in_current_level:
            counter.update(watchedVideos[id])
        return [item for item, count in sorted(list(counter.items()), key=lambda x: (x[1], x[0]))]
