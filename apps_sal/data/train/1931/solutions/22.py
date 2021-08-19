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
        s = [root]
        while s:
            t = s.pop()
            if self.dfs(head, t):
                return True
            if t:
                if t.left:
                    s.append(t.left)
                if t.right:
                    s.append(t.right)
        return False

    def dfs(self, head: ListNode, root: TreeNode) -> bool:
        # print(head.val if head else head, root.val if root else root)
        if head is None:
            return True
        if root is None:
            return False
        if root.val == head.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
        return False
