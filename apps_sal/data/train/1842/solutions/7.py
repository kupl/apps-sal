class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = collections.deque([(1, 1)])

        seen = set([1])

        level = 0

        while level < t:
            size = len(queue)
            for _ in range(size):
                f, prob = queue.popleft()
                nextCnt = 0
                for nb in graph[f]:
                    if nb not in seen:
                        nextCnt += 1
                if nextCnt == 0:
                    queue.append((f, prob))

                else:
                    for nb in graph[f]:
                        if nb not in seen:
                            queue.append((nb, prob / nextCnt))
                            seen.add(nb)
            level += 1

        ans = 0
        for node, prob in queue:
            if node == target:
                ans += prob

        return ans
