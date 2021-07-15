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
        result = False
        if not root:
            return False
        
        result = self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
        if head.val == root.val:
            l_node = head
            g_node = root
            result = result or self.match(head, root)
        
        return result
            
    def match(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        
        if not root or head.val != root.val:
            return False
        
        return self.match(head.next, root.left) or self.match(head.next, root.right)
