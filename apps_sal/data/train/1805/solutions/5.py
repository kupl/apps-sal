class Solution:
    def bfs(self, id: int, target_level: int, friends: List[List[int]], watchedVideos: List[List[str]], ans: dict):
        queue = []
        visited = []
        valid_index = 0
        queue.insert(0, id)
        visited.append(id)
        for l in range(target_level):
            new_q = []
            while len(queue) != 0:
                k = queue[0]
                del queue[0]
                for i in friends[k]:
                    if i not in visited:
                        visited.append(i)
                        new_q.append(i)
            queue[:] = new_q

        for f in queue:
            for v in watchedVideos[f]:
                if v not in ans:
                    ans[v] = 1
                else:
                    ans[v] += 1

    def dfs(self, id: int, cur_level: int, target_level: int, friends: List[List[int]], watchedVideos: List[List[str]], ans: dict, visited: List[int]):
        if id in visited:
            return
        visited.append(id)
        if cur_level == target_level:

            for v in watchedVideos[id]:
                if v not in ans:
                    ans[v] = 1
                else:
                    ans[v] += 1
            return

        for f in friends[id]:
            self.dfs(f, cur_level + 1, target_level, friends, watchedVideos, ans, visited)

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        ans = {}
        self.bfs(id, level, friends, watchedVideos, ans)
        ret = [k for k, v in sorted(list(ans.items()), key=lambda item: (item[1], item[0]))]

        return ret
