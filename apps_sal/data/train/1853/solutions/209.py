class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(set)
        for u, v, weight in edges:
            graph[u].add((v, weight))
            graph[v].add((u, weight))

        print(graph)
        dic = {}
        for num in range(n):
            queue = [(num, 0)]
            visited = {num: -1}
            count = 0
            while queue:
                node, total_weight = queue.pop(0)
                for nei, weight in graph[node]:
                    if total_weight + weight <= distanceThreshold and (nei not in visited or total_weight + weight < visited[nei]):
                        count += 1
                        queue.append((nei, total_weight + weight))
                        visited[nei] = total_weight + weight

            dic[num] = len(visited)
        print(dic)
        return sorted(list(dic.items()), key=lambda x: (x[1], -x[0]))[0][0]
