# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root==None:
            return 0
        queue=[root]
        maxval=float(\"-inf\")
        maxinde=0
        level=1
        while(queue):
            n=len(queue)
            su=sum([i.val for i in queue])
            if su>maxval:
                maxval=su
                maxinde=level 
            for i in range(n):
                x=queue.pop(0)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            level+=1
        return maxinde
            
