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
    def isSubPath(self, head: ListNode, root: TreeNode, current=None) -> bool:
        # traverse tree checking
        if head is None or root is None:
            return False
        if self.check_children(head, root):
            return True
        return (self.isSubPath(head, root.left)
                or self.isSubPath(head, root.right))

    def check_children(self, head: ListNode, root: TreeNode):
        if head is None or root is None:
            return False
        if head.val == root.val:
            if head.next is None:
                return True
            else:
                return (self.check_children(head.next, root.left)
                        or self.check_children(head.next, root.right))

        else:
            return False
