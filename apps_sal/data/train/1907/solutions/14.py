# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #     if original != None:
    #         # print(original)
    #         if original.val == target.val:
    #             print(cloned)
    #             return cloned
    #         else:
    #             right = self.getTargetCopy(original.right, cloned.right, target)
    #             left = self.getTargetCopy(original.left, cloned.left, target)
    #             return left if left else right
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = []

        def traverse(x):
            if not x:
                return False
            if x is target:
                return True
            if traverse(x.left):
                path.append(True)
                return True
            if traverse(x.right):
                path.append(False)
                return True
            return False

        traverse(original)
        pointer = cloned
        for x in reversed(path):
            if x:
                pointer = pointer.left
            else:
                pointer = pointer.right
        return pointer
