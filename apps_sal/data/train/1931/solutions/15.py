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
        def dfs(head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (dfs(head.__next__, root.left) or dfs(head.__next__, root.right))
        if not head: return True
        if not root: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
        
#         def dfs(head, root):
#             if not head:
#                 return True

#             if not root:
#                 return False

#             if root.val == head.val:
#                 return self.isSubPath(head.next, root.left) \\
#             or self.isSubPath(head.next, root.right)
#             else:
#                 return False
        
#         if not head:
#             return True

#         if not root:
#             return False
        
#         return dfs(head,root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

