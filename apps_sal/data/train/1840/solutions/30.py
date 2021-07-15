# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        l=[[root,0]]
        r=[[root,0]]
        m=0
        while(True):
            if(l==[])and(r==[]):
                return m
            l1=[]
            r1=[]
            for i in l:
                m=max(m,i[1])
                if(i[0].right!=None):
                    r1.append([i[0].right,i[1]+1])
                if(i[0].left!=None):
                    r1.append([i[0].left,0])
            for i in r:
                m=max(m,i[1])
                if(i[0].left!=None):
                    l1.append([i[0].left,i[1]+1])
                if(i[0].right!=None):
                    l1.append([i[0].right,0])
            r=r1
            l=l1
            
            

