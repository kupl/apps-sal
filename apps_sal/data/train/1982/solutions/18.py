from collections import defaultdict, deque


class Solution:
    def create_adjacency_list(self, dislikes):
        adjacency_list = defaultdict(list)
        for i, j in dislikes:
            adjacency_list[i].append(j)
            adjacency_list[j].append(i)
        return adjacency_list

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjacency_list = self.create_adjacency_list(dislikes)

        print(adjacency_list)

        color = {vertex: -1 for vertex in adjacency_list}
        print(color)

        queue = deque()

        for vertex in adjacency_list:
            if color[vertex] == -1:
                color[vertex] = 0
                queue.append(vertex)

                while queue:
                    current_node = queue.popleft()
                    for neighbor in adjacency_list[current_node]:
                        if color[neighbor] == color[current_node]:
                            return False
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[current_node]
                            queue.append(neighbor)

        return True
