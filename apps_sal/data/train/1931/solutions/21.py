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
        if head == None:
            return True
        if root == None:
            return False
        # judge root, then judge root.left and root.right
        return self.isSub(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSub(self, head, node):
        # list is over
        if head == None:
            return True
        # list is not over and tree is over
        if node == None:
            return False
        # not equal
        if not head.val == node.val:
            return False
        # equal, then left and right
        return self.isSub(head.next, node.left) or self.isSub(head.next, node.right)
