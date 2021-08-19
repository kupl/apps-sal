from collections import defaultdict


class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = defaultdict(list)
        for (i, friend_list) in enumerate(friends):
            for friend in friend_list:
                graph[i].append(friend)
                graph[friend].append(i)
        queue = [id]
        visited = set()
        visited.add(id)
        current_level = 0
        videos = defaultdict(lambda: 0)
        while queue:
            if current_level == level:
                for friend in queue:
                    for video in watchedVideos[friend]:
                        videos[video] += 1
                break
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                for friend in graph[node]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            current_level += 1
        answer = sorted(list(videos.keys()), key=lambda x: (videos[x], x))
        return answer
