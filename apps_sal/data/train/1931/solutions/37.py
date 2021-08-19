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
        if not head or not root:
            return False
        queue = deque([root])
        while queue:
            tNode = queue.pop()
            if tNode.val == head.val:
                if self.getListExistsAsPath(head, tNode):
                    return True
            if tNode.left:
                queue.appendleft(tNode.left)
            if tNode.right:
                queue.appendleft(tNode.right)
        return False

    def getListExistsAsPath(self, lNode, tNode):
        if not lNode:
            return True
        if not tNode or tNode.val != lNode.val:
            return False

        return True and (self.getListExistsAsPath(lNode.__next__, tNode.left) or self.getListExistsAsPath(lNode.__next__, tNode.right))
