class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        return head.val == root.val and (self.dfs(head.next, root.left) or self.dfs(head.next, root.right))
