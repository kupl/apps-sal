from collections import deque, Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        n = len(friends)

        stack = deque([id])
        visited = set([id])

        for _ in range(level):
            for j in range(len(stack)):
                cur = stack.popleft()
                for nxt in friends[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)

        dic = Counter()
        for ppl in stack:
            dic.update(watchedVideos[ppl])

        items = sorted(list(dic.items()), key=lambda x: (x[1], x[0]))
        return [k for k, _ in items]
