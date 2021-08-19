# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return TreeNode(val)

        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)

        return root

        # if(root==None):
        #     return TreeNode(val)
        # if(root.val<val):
        #         temp = TreeNode(val)
        #         temp.left = root
        #         return temp
        # else:
        #         root.right = self.insertIntoMaxTree(root.right, val)
        # return root
