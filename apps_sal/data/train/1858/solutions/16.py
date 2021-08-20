class FindElements:

    def __init__(self, root: TreeNode):
        li = ['null']
        self.y = set()

        def dfs(root, v):
            if root:
                root.val = v
                self.y.add(root.val)
                dfs(root.left, 2 * v + 1)
                dfs(root.right, 2 * v + 2)
        dfs(root, 0)
        print(self.y)

    def find(self, target: int) -> bool:
        if target in self.y:
            return True
        else:
            return False
