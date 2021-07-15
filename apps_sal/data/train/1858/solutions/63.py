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
        self.result = [0]
        self.dfs(self.root)
    def dfs(self,root):
        if not root:
            return
        if root.left:
            root.left.val = 2*root.val + 1
            self.result.append(root.left.val)
            self.dfs(root.left)
        if root.right:
            root.right.val = 2*root.val + 2
            self.result.append(root.right.val)
            self.dfs(root.right)

    def find(self, target: int) -> bool:
        return target in self.result
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

