class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode, current=None) -> bool:
        if head is None or root is None:
            return False
        if self.check_children(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def check_children(self, head: ListNode, root: TreeNode):
        if head is None or root is None:
            return False
        if head.val == root.val:
            if head.next is None:
                return True
            else:
                return self.check_children(head.next, root.left) or self.check_children(head.next, root.right)
        else:
            return False
