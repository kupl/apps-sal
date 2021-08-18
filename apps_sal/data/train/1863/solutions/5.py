from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.dictionary = defaultdict()

        def dfs(node, x, y):
            if not node:
                return None
            if x not in self.dictionary:
                self.dictionary[x] = defaultdict(list)
            self.dictionary[x][y].append(node.val)
            dfs(node.left, x - 1, y - 1)

            dfs(node.right, x + 1, y - 1)

        dfs(root, 0, 0)
        ans = []
        for k in sorted(self.dictionary.keys()):
            tmp = []
            for l in sorted(self.dictionary[k].keys(), key=lambda y: -y):
                tmp += sorted(self.dictionary[k][l])

            ans.append(tmp)
        return ans
