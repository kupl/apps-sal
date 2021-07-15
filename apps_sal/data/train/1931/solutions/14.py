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
        if head is None:
            return True
        if root is None:
            return False
        return self.rfun(root,head) or self.isSubPath(head,root.left) or  self.isSubPath(head,root.right)
        
    def rfun(self,root,head):
        if head is None:
            return True
        if root is None:
            return False
        return root.val == head.val and (self.rfun(root.left,head.next) or self.rfun(root.right,head.next))
