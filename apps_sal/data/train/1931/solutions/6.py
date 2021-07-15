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
    def isSubPath(self, head: ListNode, root: TreeNode, path=None, cool=None) -> bool:
        path = path or []
        cool = cool or []
        path.append(root.val)
        cool = [node.__next__ for node in cool if node.val == root.val]
        if root.val == head.val:
            cool.append(head.__next__)
            
        if None in cool:
            return True
        
        l = r = False
        if root.left:
            l = self.isSubPath(head, root.left, path.copy(), cool)
            if l is True:
                return True
        if root.right:
            r = self.isSubPath(head, root.right, path.copy(), cool)
            if r is True:
                return True

        if root.left is None and root.right is None:
            cool = []
        return False

