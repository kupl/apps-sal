class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.mapping = dict()
        for val in range(26):
            self.mapping[val] = chr(val + ord('a'))

        results = []

        self.dfs(root, [], results)
        results.sort()
        return results[0]

    def dfs(self, node, path, results):

        if not node.left and not node.right:
            path.append(node.val)
            results.append(''.join([self.mapping[i] for i in path[::-1]]))
            path.pop()
            return

        path.append(node.val)
        if node.left:
            self.dfs(node.left, path, results)
        if node.right:
            self.dfs(node.right, path, results)
        path.pop()
