from collections import deque, Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        persons = len(friends)
        visited = [False] * persons
        source = id
        visited[source] = True

        queue = deque()
        queue.append(source)
        k = 0

        videos_counter = Counter()

        while queue and k < level:

            videos_counter = Counter()
            q_len = len(queue)
            for _ in range(q_len):
                person = queue.popleft()

                for friend in friends[person]:
                    if visited[friend]:
                        continue

                    visited[friend] = True
                    queue.append(friend)
                    videos = watchedVideos[friend]
                    for video in videos:
                        videos_counter[video] += 1

            k += 1

        frequencies = [(frequency, video) for video, frequency in list(videos_counter.items())]

        result = [video for freq, video in sorted(frequencies)]
        return result
