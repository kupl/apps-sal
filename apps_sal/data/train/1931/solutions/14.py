class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        return self.rfun(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def rfun(self, root, head):
        if head is None:
            return True
        if root is None:
            return False
        return root.val == head.val and (self.rfun(root.left, head.next) or self.rfun(root.right, head.next))
