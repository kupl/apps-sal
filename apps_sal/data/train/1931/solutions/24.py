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

        visited = set()

        def checkNode(treePointer, listPointer):
            if listPointer == None:
                return True
            if treePointer == None and listPointer != None:
                return False

            if (treePointer, listPointer) in visited:
                return False

            if treePointer.val == listPointer.val:
                if checkNode(treePointer.left, listPointer.next) or checkNode(treePointer.right, listPointer.next):
                    return True

            if treePointer.val == head.val:
                if checkNode(treePointer.left, head.next) or checkNode(treePointer.right, head.next):
                    return True

            if checkNode(treePointer.left, head) or checkNode(treePointer.right, head):
                return True

            visited.add((treePointer, listPointer))
            return False

        return checkNode(root, head)
