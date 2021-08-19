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
    def isSubPathHelper(self, cur, root):
        if not cur:
            return True
        if not root:
            return False
        return cur.val == root.val and (self.isSubPathHelper(cur.__next__, root.left) or self.isSubPathHelper(cur.__next__, root.right))

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        found = self.isSubPathHelper(head, root)
        nodes = []
        if root.left:
            nodes.append(root.left)
        if root.right:
            nodes.append(root.right)
        for node in nodes:
            found |= self.isSubPath(head, node)
        return found
