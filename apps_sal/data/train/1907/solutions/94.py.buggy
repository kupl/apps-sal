# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned

        self.path = \"\"
        self.found = False
        def getTargetCopyRecursive(root, path, target):
            if root and not self.found:
                if root == target:
                    self.found = True
                    self.path = path
                else:
                    if root.right and not self.found:
                        getTargetCopyRecursive(root.right, path + \"R\", target)
                    if root.left and not self.found:
                        getTargetCopyRecursive(root.left, path + \"L\", target)

        getTargetCopyRecursive(original,\"\",target)

        root = cloned
        for letter in self.path:
            if letter == \"R\":
                root = root.right
            elif letter == \"L\":
                root = root.left

        return root
