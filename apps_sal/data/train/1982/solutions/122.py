class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for f, to in dislikes:
            graph[f].append(to)
            graph[to].append(f)

        group = collections.defaultdict(bool)
        curr_group = True
        for i in range(1, N + 1):
            if i not in group:
                q = collections.deque([i])
                group[i] = curr_group
                while q:
                    for _ in range(len(q)):
                        node = q.popleft()
                        for nei in graph[node]:
                            if nei in group and group[nei] == curr_group:
                                return False
                            elif nei not in group:
                                q.append(nei)
                                group[nei] = not curr_group
                    curr_group = not curr_group
        return True
