from collections import defaultdict, deque


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set()
        queue = deque([(id, 0)])
        visited.add(id)
        chosenFriends = list()
        while queue:
            person, lv = queue.popleft()
            if lv == level:
                chosenFriends.append(person)
            if lv > level:
                break
            for friend in friends[person]:
                if friend not in visited:
                    queue.append((friend, lv + 1))
                    visited.add(friend)
        videoFrequency = defaultdict(int)
        for friend in chosenFriends:
            for video in watchedVideos[friend]:
                videoFrequency[video] += 1
        return [video[0] for video in sorted(list(videoFrequency.items()), key=lambda x: (x[1], x[0]))]
