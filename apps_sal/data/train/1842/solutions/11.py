class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        table = {}
        for i in range(1, n + 1):
            table[i] = []
        for i in range(len(edges)):
            table[edges[i][0]].append(edges[i][1])
            table[edges[i][1]].append(edges[i][0])

        self.res = 0

        def DFS(current_node, p, visited, time):
            if time == t:
                if current_node == target:
                    self.res += p
            elif time < t:
                temp = 0
                for node in table[current_node]:
                    if node not in visited:
                        temp += 1
                if temp > 0:
                    for node in table[current_node]:
                        if node not in visited:
                            temp_visited = visited[:]
                            temp_visited.append(node)
                            DFS(node, p * 1 / temp, temp_visited, time + 1)
                elif temp == 0:
                    DFS(current_node, p, visited, time + 1)

        DFS(1, 1, [1], 0)

        return self.res
