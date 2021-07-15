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
        def dfs(cur, node):
            if not cur:
                return True
            if not node:
                return False
            if cur.val == node.val:
                return dfs(cur.__next__, node.left) or dfs(cur.__next__, node.right)
            return False
        stack = [root]
        while stack:
            for node in stack:
                cur = head
                if dfs(cur, node):
                    return True
            stack = [leaf for node in stack for leaf in [node.left, node.right] if leaf]
        return False

