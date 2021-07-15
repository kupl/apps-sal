# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Also recursive.
Base case: old tree is empty
    - TreeNode(new elem, None, None)
Case 1: new elem > max elem in tree.
    - Then new tree should be TreeNode(new elem, old tree, None)
Case 2: new elem < max elem in tree
    - Then right subtree needs to be updated (recurse)
    - New tree = TreeNode(max elem, left subtree, new right subtree)
'''


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val, None, None)
        if val > root.val:
            return TreeNode(val, root, None)
        else:
            # val < root.val
            return TreeNode(root.val, root.left, self.insertIntoMaxTree(root.right, val))
