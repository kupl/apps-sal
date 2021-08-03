# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
