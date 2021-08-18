class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        graph = collections.defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)

        for y in range(1, n + 1):
            if y != x:
                visited = set()
                stack = [x]
                while stack:
                    val = stack.pop()
                    visited.add(val)
                    for nei in graph[val]:
                        if nei not in visited and nei != y:
                            stack.append(nei)

                if len(visited) <= n // 2:
                    return True

        return False
