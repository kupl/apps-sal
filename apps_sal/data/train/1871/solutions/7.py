# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root):
            if(root == None):
                return([])
            left = helper(root.left)
            right = helper(root.right)
            temp = []
            for i in range(len(left)):
                if(abs(left[i] - root.val) > self.ans):
                    self.ans = abs(left[i] - root.val)
                temp.append(left[i])
            for i in range(len(right)):
                if(abs(right[i] - root.val) > self.ans):
                    self.ans = abs(right[i] - root.val)
                temp.append(right[i])
            temp.append(root.val)
            return(temp)
        self.ans = 0
        helper(root)
        return(self.ans)
