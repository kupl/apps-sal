class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(node):
            if not node:
                return
            if node.val == head.val:
                q.appendleft((node, head, set()))
            dfs(node.left)
            dfs(node.right)

        q = collections.deque()
        dfs(root)

        while q:
            tree_node, list_node, visited = q.pop()
            if tree_node.val == list_node.val:
                if not list_node.__next__:
                    return True
                for nei in (tree_node.left, tree_node.right):
                    if nei and nei not in visited and nei.val == list_node.next.val:
                        visited.add(nei)
                        q.appendleft((nei, list_node.__next__, visited))
                        visited.remove(nei)
        return False
