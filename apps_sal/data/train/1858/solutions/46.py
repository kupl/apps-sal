# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def __init__(self, root: TreeNode):
        self.values=[]
        self.tree=root
        
        def preorder(node, value):
            self.values.append(value)
            node.val=value
            if node.left:
                preorder(node.left, value*2+1)
            if node.right:
                preorder(node.right, value*2+2)
        
        preorder(root, 0)
        
        
    def find(self, target: int) -> bool:
        return target in self.values
                

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

