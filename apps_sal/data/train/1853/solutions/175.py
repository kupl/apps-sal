class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = [[] for i in range(n)]
        for src, dst, weight in edges:
            graph[src].append((weight, dst))
            graph[dst].append((weight, src))

        def find_num_closest(city):
            visited = set()
            q = [(0, city)]
            while q:
                dist, c = heappop(q)
                if c in visited:
                    continue
                visited.add(c)
                for weight, dest in graph[c]:
                    if dist + weight <= threshold:
                        heappush(q, (dist + weight, dest))
            return len(visited)

        min_val = float('inf')
        min_city = None
        for i in range(n):
            closest = find_num_closest(i)
            #print(\"city {} has {} within threshold\".format(i, closest))
            if closest <= min_val:
                min_val = closest
                min_city = i
        return min_city
