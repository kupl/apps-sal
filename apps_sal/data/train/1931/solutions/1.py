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
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        t = [-1]
        pos, cnd = 1, 0
        while pos < len(arr):
            if arr[pos] == arr[cnd]:
                t.append(t[cnd])
            else:
                t.append(cnd)
                cnd = t[cnd]
                while cnd >= 0 and arr[pos] != arr[cnd]:
                    cnd = t[cnd]
            pos += 1
            cnd += 1
        t.append(cnd)

        def dfs(root, i):
            if i == len(arr):
                return True
            if root is None:
                return False
            while i >= 0 and root.val != arr[i]:
                i = t[i]
            return dfs(root.left, i + 1) or dfs(root.right, i + 1)

        return dfs(root, 0)
