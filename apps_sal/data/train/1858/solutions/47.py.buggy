# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.values = []
        self.__init(self.root)
        
    def __init(self, node):
        if node.left:
            value = 2 * node.val + 1
            node.left.val = value
            self.values.append(value)
            self.__init(node.left)
            
        if node.right:
            value = 2 * node.val + 2
            node.right.val = value
            self.values.append(value)
            self.__init(node.right)

            
    def __find(self, node, target) -> bool:
        if not node: 
            return False
        
        if node.val == target:
            return True
        
        return self.__find(node.left, target) \\
            or self.__find(node.right, target)
    
    def find(self, target: int) -> bool:
        return target in self.values
        # return self.__find(self.root, target)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
