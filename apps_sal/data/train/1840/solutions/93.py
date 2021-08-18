class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        nodes = self.bfs(root)
        self.dp = {node: [False, False] for node in nodes}
        ans = 0
        for x in range(len(nodes)):
            ans = max(ans, self.recur(0, nodes[x], -1), self.recur(1, nodes[x], -1))
        return ans

    def bfs(self, node):
        q = [node]
        arr = []
        while q:
            r = q.pop()
            arr.append(r)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        return arr

    def recur(self, p, node, c):
        if not node:
            return c
        if self.dp[node][p] != False:
            return self.dp[node][p]

        if p == 0:
            self.dp[node][p] = self.recur(p ^ 1, node.left, c + 1)
            return self.dp[node][p]
        else:
            self.dp[node][p] = self.recur(p ^ 1, node.right, c + 1)
            return self.dp[node][p]
