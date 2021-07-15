# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __decontaminate(self, node, val):
        if not node:
            return
        node.val = val
        self.__decontaminate(node.left, 2*node.val + 1)
        self.__decontaminate(node.right, 2*node.val + 2)
        
    def __init__(self, root: TreeNode):
        self.__decontaminate(root, 0)
        self.root = root
    
    def __trav(self, node, index, path):
        if index == len(path):
            return True
        if not node:
            return False
        if path[index] == node.val:
            l = self.__trav(node.left, index+1, path)
            r = self.__trav(node.right, index+1, path)
            return l or r
        else:
            return False
        
    def find(self, target: int) -> bool:
        path = [target]
        while target:
            diff = 1 if target%2 else 2
            target = int((target-diff)/2)
            path.append(target)
        path.reverse()
        return self.__trav(self.root, 0, path)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

