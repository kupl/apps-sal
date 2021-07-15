# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.visited = set()
        
    def zigzagPath(self,node,direction):
        
        length = 0
        while node:
                
            if direction ==1:
                node = node.right
                if node and node.left:
                    self.visited.add((node,\"left\"))
            elif direction ==0:
                node = node.left
                if node and node.right:
                    self.visited.add((node,\"right\"))
            direction = 1 - direction
            if node!=None:
                length+=1
        return length
        
    
    def longestZigZag(self, root: TreeNode) -> int:
        max_length = 0
        S = [root]
        while S:
            node = S.pop(0)
            if node.right: 
                if (node,\"right\") not in self.visited:
                    max_length = max(self.zigzagPath(node,1),max_length)
                self.visited.add((node,\"right\"))
                S.append(node.right)
            if node.left: 
                if (node,\"left\") not in self.visited:
                    max_length = max(self.zigzagPath(node,0),max_length)
                self.visited.add((node,\"left\"))
                S.append(node.left)
        return max_length
        
        
