from collections import deque, Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        all_video = 0
        videos_dict = {}
        queue = deque([id])
        visited = set()
        visited.add(id)
        current_level = 0

        friends_dict = {id: []}

        while queue:
            level_size = len(queue)
            level_friends = queue
            for _ in range(level_size):
                cur_node = queue.popleft()
                for friend in friends[cur_node]:
                    if friend in visited:
                        continue
                    queue.append(friend)
                    visited.add(friend)
            current_level += 1
            print(current_level)

            if current_level == level:
                break
        print(('friends', queue))
        for friend in queue:

            for video in watchedVideos[friend]:
                if video in videos_dict:
                    videos_dict[video] += 1
                else:
                    videos_dict[video] = 1

        return sorted(videos_dict, key=lambda x: (videos_dict[x], x), reverse=False)
