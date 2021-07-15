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
        @lru_cache(maxsize=None)
        def helper(llNode, tNode) -> bool:
            if not llNode:
                return True
            if not tNode:
                return False
            result = False
            nonlocal head
            # print(llNode.val, tNode.val, head.val)
            if tNode.val == llNode.val:
                result = result \\
                    or helper(llNode.next, tNode.left) \\
                    or helper(llNode.next, tNode.right)
            if tNode.val == head.val:
                result = result \\
                    or helper(head.next, tNode.left) \\
                    or helper(head.next, tNode.right)
            else:
                result = result \\
                    or helper(head, tNode.left) \\
                    or helper(head, tNode.right)

            return result
        
        return helper(head, root)
        
