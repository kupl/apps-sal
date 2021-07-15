# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxel = -float('inf')
        
        def traverse(root,anc,maxel):
            if root:
            
                for i in anc:
                    val = abs(i-root.val)
                    # print(val,maxel)
                    maxel = max(maxel,val)
                anc.append(root.val)
                maxel = traverse(root.right,anc,maxel)
                maxel = traverse(root.left,anc,maxel)
                anc.pop(-1)
            return maxel
        return traverse(root,[],maxel)
                

