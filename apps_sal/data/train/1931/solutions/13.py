class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            if root.val == head.val:
                return dfs(head.next, root.left) or dfs(head.next, root.right)
        if not head:
            return True
        if not root:
            return False
        if dfs(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
