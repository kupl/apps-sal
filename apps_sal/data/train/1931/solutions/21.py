class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        return self.isSub(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSub(self, head, node):
        if head == None:
            return True
        if node == None:
            return False
        if not head.val == node.val:
            return False
        return self.isSub(head.next, node.left) or self.isSub(head.next, node.right)
