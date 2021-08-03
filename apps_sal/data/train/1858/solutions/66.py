# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.vals = []
        self.createTree(root, 0)

    def createTree(self, root, val):
        root.val = val
        self.vals.append(val)
        if root.left is not None:
            self.createTree(root.left, 2 * root.val + 1)

        if root.right is not None:
            self.createTree(root.right, 2 * root.val + 2)

    def find(self, target: int) -> bool:
        return target in self.vals
        # return self.findRec(target, self.root)

    def findRec(self, target, root):
        if root.val == target:
            # print(\"val\", root.val)
            # print(\"target\", target)
            # print(\"match\")
            return True
        if root.left is not None:
            if self.findRec(target, root.left):
                # print(\"val\", root.val)
                # print(\"target\", target)
                # print(\"leftChildMatch\")
                return True
        if root.right is not None:
            if self.findRec(target, root.right):
                # print(\"val\", root.val)
                # print(\"target\", target)
                # print(\"rightChildMatch\")
                return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
