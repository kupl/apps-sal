# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        
        self.val =  []
        root.val = 0 
        self.root = self.helper(root) #use dictionary to store vals
        
        
        
    def helper(self,root):
        if root:
            self.val.append(root.val)
            if root.left:
                root.left.val = 2 * root.val + 1
                l = self.helper(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                r = self.helper(root.right)
            return root
        return 
        

    def find(self, target: int) -> bool:
        
        return target in self.val


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

