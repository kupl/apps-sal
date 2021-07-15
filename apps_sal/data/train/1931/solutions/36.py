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
    def _iter(self, root):
        if root is not None:
            yield root
            yield from self._iter(root.left)
            yield from self._iter(root.right)
    
    def _search(self, head, root):
        if head is None or root is None:
            return head is None
        elif head.val == root.val:
            return self._search(head.next, root.left) or self._search(head.next, root.right)
        else:
            return False
        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        for node in self._iter(root):
            if node.val == head.val:
                if self._search(head, node):
                    return True
        return False
