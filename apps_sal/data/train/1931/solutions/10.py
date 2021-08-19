class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
