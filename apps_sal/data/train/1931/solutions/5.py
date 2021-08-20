class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def fromHeadPath(h, r):
            if not h or not r:
                return False
            if h.val != r.val:
                return False
            if not h.__next__:
                return True
            return fromHeadPath(h.__next__, r.left) or fromHeadPath(h.__next__, r.right)
        if not head or not root:
            return False
        if fromHeadPath(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
