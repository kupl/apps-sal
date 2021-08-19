from collections import deque, Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # Var def
        all_video = 0
        videos_dict = {}
        queue = deque([id])
        visited = set()
        visited.add(id)
        current_level = 0

        # Create friends dict (for BFS)
        friends_dict = {id: []}

        # Get all friends at K level
        while queue:  # 1, 2
            level_size = len(queue)  # len=2
            level_friends = queue
            for _ in range(level_size):  # [1, 2]
                cur_node = queue.popleft()  # 2
                for friend in friends[cur_node]:  # 3
                    if friend in visited:
                        continue
                    queue.append(friend)
                    visited.add(friend)  # 3
            current_level += 1  # 2
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

        # print(videos_dict)
        #print(sorted(videos_dict.items(), key=lambda x:(videos_dict[x], x[1]))   )
        #print(sorted(videos_dict, key=lambda x: videos_dict[x], reverse=False))
        return sorted(videos_dict, key=lambda x: (videos_dict[x], x), reverse=False)

        #videos_dict = Counter('abcdaab')

        # Get the movies watch by that level of friends

        # Ordering
