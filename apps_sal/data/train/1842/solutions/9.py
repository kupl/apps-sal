class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = collections.deque()
        q.append((1, 1.0))
        visited = set()
        visited.add(1)
        
        step = 0
        while q and step <= t:
            size = len(q)
            for _ in range(size):
                i, prob = q.popleft()
                if step == t and i == target:
                    return prob

                count = 0
                if i == 1:
                    count = len(graph[i])
                else:
                    count = len(graph[i]) - 1
                
                if count == 0:
                    q.append((i, prob))
                    continue
                
                for neighbor in graph[i]:
                    if neighbor not in visited:
                        q.append((neighbor, prob / count))
                        visited.add(neighbor)
                
            step += 1
        
        return 0.0
