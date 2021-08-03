# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0
    def goodNodes(self, root: TreeNode) -> int:
        current=root.val
        
        path=[]
        path.append(float('-inf'))
        \"\"\" append min val in to path and check if root val gretaer or == to max(path) if true increase count by 1 and add root to path.
        recursively call root.left and root.right and pop the top element)\"\"\"
        def good(path,root):
            if root is None:
                return
            if root.val>=max(path):
                self.count=self.count+1
            path.append(root.val)
                #print(root.val)
            good(path,root.right)
            good(path,root.left)
            path.pop()
            return self.count
        #print(self.count)
        return good(path,root)
            
                          
            
                    
                          
            
        
