# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.tot_val = []

        def dfs(root, new_val):
            if not root:
                return
            root.val = new_val
            self.tot_val.append(new_val)
            if root.left:
                dfs(root.left, new_val * 2 + 1)
            if root.right:
                dfs(root.right, new_val * 2 + 2)
        self.root = root
        dfs(self.root, 0)

    def find(self, target: int) -> bool:
        if target in self.tot_val:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
