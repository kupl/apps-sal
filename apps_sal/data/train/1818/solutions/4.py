class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, path):
            nonlocal ans
            if node:
                path.append(letter_map[node.val])
                if not node.left and not node.right:
                    path_str = ''.join(reversed(path))
                    if not ans:
                        ans = path_str
                    elif path_str < ans:
                        ans = path_str
                else:
                    pre_path = path.copy()
                    if node.left:
                        dfs(node.left, path)
                    if node.right:
                        dfs(node.right, pre_path)
        letter_map = []
        letter = 'a'
        for i in range(26):
            letter_map.append(letter)
            letter = chr(ord(letter) + 1)

        ans = None
        dfs(root, [])

        return ans
