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
        paths = []
        def dfs(root, arr):
            arr1 = arr + [str(root.val)]
            if root.left:
                dfs(root.left, arr1)
            if root.right:
                dfs(root.right, arr1)
            if not root.left and not root.right:
                paths.append(arr1)
        dfs(root, [])
        target = []
        while head:
            target.append(str(head.val))
            head = head.next
        tar = '#'.join(target)
        for path in paths:
            if tar in '#'.join(path):
                return True
        return False
