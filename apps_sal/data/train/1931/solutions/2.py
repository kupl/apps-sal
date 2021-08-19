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
        def dfs(root, head):
            if not root and not head:
                return True
            if not head and root:
                return True
            if not root and head:
                return False
            if root.val != head.val:
                return False
            left = dfs(root.left, head.__next__)
            right = dfs(root.right, head.__next__)
            return left or right

        if not root:
            return False
        if dfs(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
