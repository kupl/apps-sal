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
        Head = head

        @lru_cache(None)
        def helper(root, head):
            if(head is None):
                return True
            if(root is None):
                return False
            ans = False
            if(root.val == head.val):
                ans = ans or helper(root.left, head.__next__)
                ans = ans or helper(root.right, head.__next__)
            ans = ans or helper(root.left, Head)
            ans = ans or helper(root.right, Head)
            return ans
        return helper(root, head)
