# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        ans = 0
        nodes = [root]
        self.dp = {}
        while(len(nodes)!=0):
            tmp = []
            for node in nodes:
                if(node.left is not None):
                    tmp.append(node.left)
                if(node.right is not None):
                    tmp.append(node.right)
                ans = max(ans, self.helper(node,1))
                ans = max(ans, self.helper(node,0))
            nodes = tmp
        return ans-1
        
    def helper(self,node,status):
        if(node is None):
            return 0
        if((node,status) in self.dp):
            return self.dp[(node,status)]
        if(status == 1):
            ans = self.helper(node.right,0)
        else:
            ans = self.helper(node.left, 1)
        self.dp[(node,status)]  = 1 + ans
        return 1+ans
