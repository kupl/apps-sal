class FindElementsDict:

    def dfs_recover(self, root: TreeNode):
        if not root:
            return
        if root.left is not None:
            root.left.val = 2 * root.val + 1
            self.all_values.add(root.left.val)
        if root.right is not None:
            root.right.val = 2 * root.val + 2
            self.all_values.add(root.right.val)
        self.dfs_recover(root.left)
        self.dfs_recover(root.right)

    def __init__(self, root: TreeNode):
        self.all_values = {}
        if root:
            root.val = 0
            self.all_values = {root.val}
        self.dfs_recover(root)

    def find(self, target: int) -> bool:
        return target in self.all_values


class FindElements:

    def dfs_recover(self, root: TreeNode):
        if not root:
            return
        if root.left is not None:
            root.left.val = 2 * root.val + 1
            self.all_values[root.left.val] = True
        if root.right is not None:
            root.right.val = 2 * root.val + 2
            self.all_values[root.right.val] = True
        self.dfs_recover(root.left)
        self.dfs_recover(root.right)

    def __init__(self, root: TreeNode):
        self.all_values = [False] * 2097152
        if root:
            root.val = 0
            self.all_values[root.val] = True
        self.dfs_recover(root)

    def find(self, target: int) -> bool:
        return self.all_values[target]
