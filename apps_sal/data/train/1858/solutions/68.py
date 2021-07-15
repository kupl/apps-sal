# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        def helper(root,val):
            if root is None:
                return 
            root.val=val
            helper(root.left,2*val+1)
            helper(root.right,2*val+2)
        helper(root,0)
        self.array=[]
        
        def help(root):
            if root is None:
                return
            help(root.left)
            self.array.append(root.val)
            help(root.right)
        help(root)   
        
        

    def find(self, target: int) -> bool:
        if target in self.array:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

