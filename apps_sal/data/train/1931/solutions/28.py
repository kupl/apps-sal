class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(nodeL, nodeT):
            if not nodeT and nodeL:
                return False
            if not nodeL:
                return True
            if nodeL.val == nodeT.val:
                return dfs(nodeL.next, nodeT.left) or dfs(nodeL.next, nodeT.right)

            return False

        bfs = collections.deque([root])
        while bfs:
            node = bfs.popleft()
            if dfs(head, node):
                return True
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return False
