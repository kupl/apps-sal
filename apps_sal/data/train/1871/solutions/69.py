# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,output,maxValue):
        if(root is None):
            return 
        for ele in output:
            if(abs(root.val-ele)>maxValue[0]):
                maxValue[0]=abs(root.val-ele)
        # if(len(output)>1):
        #     ele1=output[-1]
        #     ele2=output[-2]
        #     if(abs(root.val-ele1)>maxValue[0]):
        #         maxValue[0]=abs(root.val-ele1)
        #     if(abs(root.val-ele2)>maxValue[0]):
        #         maxValue[0]=abs(root.val-ele2)
        # elif(len(output)==1):
        #     ele1=output[-1]
            # if(abs(root.val-ele1)>maxValue[0]):
            #     maxValue[0]=abs(root.val-ele1)
        output.append(root.val)
        self.helper(root.left,output,maxValue)
        self.helper(root.right,output,maxValue)
        output.pop()
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxValue=[0]
        output=list()
        self.helper(root,output,maxValue)
        return maxValue[0]

