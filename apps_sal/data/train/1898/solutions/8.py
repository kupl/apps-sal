# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # from collections import deque
        # queue = deque([root])
        # visited = []
        # while queue:
        #     curr = queue.popleft()
        #     if curr:
        #         visited.append(curr)
        #         queue.extend([curr.left, curr.right])
        # res = []
        # for node in visited:
        #     if node.val in to_delete:
        #         if node.left: res.append(node.left)
        #         if node.right: res.append(node.right)
        #         node = None
        # if root and root.val not in to_delete:
        #     res.append(root)
        # return res

        stack = [(root, True)]
        res = []
        while stack:
            curr, toBeRoot = stack.pop()
            if curr:
                if curr.val not in to_delete and toBeRoot:
                    res.append(curr)
                toBeRoot = curr.val in to_delete
                stack += [(curr.left, toBeRoot), (curr.right, toBeRoot)]
                if curr.left and curr.left.val in to_delete:
                    curr.left = None
                if curr.right and curr.right.val in to_delete:
                    curr.right = None

        return res
