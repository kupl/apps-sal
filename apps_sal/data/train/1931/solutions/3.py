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
        # find the beginning of list node in tree. then traverse
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
