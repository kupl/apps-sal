class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        def aux(root, isleft, memo):
            if not root:
                return 0
            if root in memo:
                if isleft:
                    return memo[root][1]
                else:
                    return memo[root][0]
            memo[root] = [0, 0]
            memo[root][0] = aux(root.left, 1, memo) + 1
            memo[root][1] = aux(root.right, 0, memo) + 1
            self.ans = max(self.ans, memo[root][1], memo[root][0])
            if isleft:
                return memo[root][1]
            else:
                return memo[root][0]

        if not root:
            return 0
        memo = {}
        aux(root, 0, memo)
        return self.ans - 1
