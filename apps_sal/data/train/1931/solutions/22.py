class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        s = [root]
        while s:
            t = s.pop()
            if self.dfs(head, t):
                return True
            if t:
                if t.left:
                    s.append(t.left)
                if t.right:
                    s.append(t.right)
        return False

    def dfs(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        if root.val == head.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
        return False
