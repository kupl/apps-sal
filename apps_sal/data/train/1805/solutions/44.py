class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        queue.append([id, 0])
        ans = defaultdict(int)
        visited = {id: 1}
        while len(queue) > 0:
            (now, l) = queue.popleft()
            if l == level:
                for v in watchedVideos[now]:
                    ans[v] += 1
                continue
            for friend in friends[now]:
                if friend not in visited:
                    queue.append([friend, l + 1])
                    visited[friend] = 1
        ansid = sorted(ans.items(), key=lambda x: (x[1], x[0]))
        ansid = [x for (x, _) in ansid]
        return ansid
