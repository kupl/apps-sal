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
        memo = {}

        def _isSubPath(head, listnode, root):
            if listnode is None:
                return True

            if root is None:
                return False

            if (listnode, root) in memo:
                return memo[(listnode, root)]

            ret = False
            if root.val == listnode.val:
                ret = _isSubPath(head, listnode.__next__, root.left) or _isSubPath(head, listnode.__next__, root.right)

            ret = ret or _isSubPath(head, head, root.left) or _isSubPath(head, head, root.right)
            memo[(listnode, root)] = ret
            return ret

        return _isSubPath(head, head, root)
