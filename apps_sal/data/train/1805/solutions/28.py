class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        stack = deque([id])
        seen = set()
        seen.add(id)
        for _ in range(level):
            for i in range(len(stack)):
                f = stack.popleft()
                for j in friends[f]:
                    if j not in seen:
                        stack.append(j)
                        seen.add(j)
        
        count = Counter()
        for lf in stack:
            count += Counter(watchedVideos[lf])
        return [x[0] for x in sorted(count.items(), key=lambda item: (item[1], item[0]))]
