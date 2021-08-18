class FindElements:
    def __init__(self, R: TreeNode):
        R.val, V = 0, set()

        def dfs(R):
            if R == None or R.left is R.right:
                return
            if R.left != None:
                R.left.val, _ = 2 * R.val + 1, V.add(2 * R.val + 1)
            if R.right != None:
                R.right.val, _ = 2 * R.val + 2, V.add(2 * R.val + 2)
            dfs(R.left), dfs(R.right)
        dfs(R)
        self.V = V

    def find(self, t: int) -> bool: return t in self.V
