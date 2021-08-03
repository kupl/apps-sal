# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        \"\"\"
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        \"\"\"
        if not root:
            return root
        res = []
        self.dfs(root, to_delete, res)
        if root.val not in to_delete:
            res.append(root)
        return res
    
    def dfs(self, root, to_delete, res):
        if not root:
            return
        root.left = self.dfs(root.left, to_delete, res)
        root.right = self.dfs(root.right, to_delete, res)
        if root.val in to_delete:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        return root
