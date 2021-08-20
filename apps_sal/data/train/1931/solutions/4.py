class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(p, q):
            if not p:
                return True
            if not q or p.val != q.val:
                return False
            if p.val == q.val:
                return dfs(p.__next__, q.right) or dfs(p.__next__, q.left)
            return False
        if not root:
            return False
        if not head:
            return True
        return dfs(head, root) or self.isSubPath(head, root.right) or self.isSubPath(head, root.left)
