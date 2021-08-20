class Solution:

    def find(self, root, d, s, h):
        if root == None:
            return None
        if h not in list(d.keys()):
            d[h] = root.val
        else:
            d[h] = d[h] + root.val
        self.find(root.left, d, s, h + 1)
        self.find(root.right, d, s, h + 1)

    def maxLevelSum(self, root: TreeNode) -> int:
        d = dict()
        s = [0]
        self.find(root, d, s, 1)
        return max(d, key=d.get)
