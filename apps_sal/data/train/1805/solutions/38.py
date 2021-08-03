from collections import Counter, deque
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque([(0, id)])
        seen = [False] * len(friends)
        d = dict()

        while q:
            stage, person = q.popleft()
            seen[person] = True
            if stage not in d:
                d[stage] = set()

            d[stage].add(person)

            for friend in friends[person]:
                if seen[friend]:
                    continue
                seen[friend] = True
                q.append((stage + 1, friend))

        shared = dict()
        for friend in d[level]:
            for video in watchedVideos[friend]:
                if video in shared:
                    shared[video] += 1
                else:
                    shared[video] = 1
        return list(x for _, x in sorted((freq, val) for val, freq in shared.items()))
