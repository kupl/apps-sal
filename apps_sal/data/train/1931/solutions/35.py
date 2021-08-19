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
    # Time Complextity O(root)*O(head)
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        helper = set()

        # Find all possible start
        def getStart(p):
            if p:
                if p.val == head.val:
                    helper.add(p)
                getStart(p.left)
                getStart(p.right)

        # Main
        getStart(root)
        # print(helper)

        while head.next:
            new = set()
            for node in helper:
                if node.val == head.val:
                    if node.left:
                        new.add(node.left)
                    if node.right:
                        new.add(node.right)
            helper = new

            if not helper:
                return False

            head = head.next

        return (head.val in [node.val for node in helper])
