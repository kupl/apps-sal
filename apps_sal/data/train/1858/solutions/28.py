# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        res = {}

        def helper(node, parent=None, left=False, right=False):
            if node:
                if parent is None:
                    node.val = 0  # root
                    res[node.val] = 1
                else:
                    if left:
                        node.val = parent.val * 2 + 1
                        res[node.val] = 1
                    if right:
                        node.val = parent.val * 2 + 2
                        res[node.val] = 1
                helper(node.left, node, True, False)
                helper(node.right, node, False, True)
        helper(root)
        self.res = res
        print(root)

    def find(self, target: int) -> bool:
        return target in self.res


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
