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
        def helper(temp, root):
            if not temp:
                return 1
            if not root:
                return 0
            if root.val == temp.val:
                a = helper(temp.__next__, root.left)
                b = helper(temp.__next__, root.right)
                return a or b
            return 0

        def fun(head, root):
            temp = head
            if not root:
                return 0
            if helper(temp, root):
                return 1
            a = fun(head, root.left)
            b = fun(head, root.right)
            return a or b
        return fun(head, root)
