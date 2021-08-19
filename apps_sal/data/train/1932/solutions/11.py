class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        if not root:
            return False
        from collections import defaultdict
        graph = defaultdict(list)

        def convert_tree_to_graph(root, parent=None):
            if not root:
                return None
            if parent:
                graph[parent].append(root)
                graph[root].append(parent)
            if root.left:
                convert_tree_to_graph(root.left, root)
            if root.right:
                convert_tree_to_graph(root.right, root)
        convert_tree_to_graph(root)
        node = None
        for (g, v) in list(graph.items()):
            if g.val == x:
                node = g
                break

        def count_nodes_in_subtree(node, visited):
            if node in visited or node.val == x:
                return 0
            visited.add(node)
            count = 0
            for neighbor in graph[node]:
                if neighbor not in visited:
                    count += count_nodes_in_subtree(neighbor, visited)
            return count + 1
        subtrees = []
        max_subtree = -1
        for subtree in graph[node]:
            ans = count_nodes_in_subtree(subtree, set())
            subtrees.append(ans)
            max_subtree = max(max_subtree, ans)
        return n - max_subtree < max_subtree
        if not subtrees:
            return False
        if len(subtrees) == 1 and subtrees[0] > 1:
            return True
        return False
