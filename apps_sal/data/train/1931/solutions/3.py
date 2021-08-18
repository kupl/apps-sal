class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def helper(lNode, TNode):
            if not lNode:
                return True
            if not TNode:
                return False
            return TNode.val == lNode.val and (
                helper(lNode.next, TNode.left) or helper(lNode.next, TNode.right)
            )

        if not head:
            return True
        if not root:
            return False
        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
