# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.elements = []

        def traverse(node, x):
            self.elements.append(x)
            if node.left != None:
                traverse(node.left, 2 * x + 1)
            if node.right != None:
                traverse(node.right, 2 * x + 2)
        traverse(root, 0)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
