class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True

        nodeMap = {}

        for a, b in dislikes:
            if a not in nodeMap:
                nodeMap[a] = Node(a)

            if b not in nodeMap:
                nodeMap[b] = Node(b)

            nodeMap[a].connections.append(nodeMap[b])
            nodeMap[b].connections.append(nodeMap[a])

        visited = set()
        colored = {}

        def dfs(queue: List[Node]) -> bool:
            if len(queue) == 0:
                return True

            node = queue.pop()
            # print(node)

            if node in visited:
                return dfs(queue)

            visited.add(node)

            color = 1
            if node in colored:
                color = colored[node]

            for connect in node.connections:
                if connect in colored:
                    if colored[connect] == color:
                        return False
                else:
                    colored[connect] = 1 - color

                if connect not in visited:
                    queue.append(connect)
            return dfs(queue)

        for key, val in list(nodeMap.items()):
            # print(val)
            if val in visited:
                continue
            else:
                res = dfs([val])
                if not res:
                    return False
        return True


class Node:
    def __init__(self, val):
        self.val = val
        self.connections = []
