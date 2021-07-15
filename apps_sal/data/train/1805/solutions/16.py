class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = collections.defaultdict(list)
        for u, v in enumerate(friends):
            for i in v:
                graph[u].append(i)
        queue = collections.deque()
        queue.append((id, 0))
        visited = set()
        visited.add(id)
        res = collections.defaultdict(int)
        while queue:
            id, l = queue.popleft()
            if l == level:
                for j in watchedVideos[id]:
                    res[j] += 1
            for v in graph[id]:
                if l+1 <= level and v not in visited:
                    visited.add(v)
                    queue.append((v, l+1))
        from functools import cmp_to_key
        def func(x, y):
            if res[x] > res[y]:
                return -1
            elif res[y] > res[x]:
                return 1
            else:
                if x > y:
                    return -1
                elif y > x:
                    return 1
                else:
                    return 0
        return (sorted(res.keys(), key=cmp_to_key(func)))[::-1]
