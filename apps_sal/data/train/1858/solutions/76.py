# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def recover(self, root):
        if not root:
            return

        x = root.val

        if root.left:
            node_val = 2 * x + 1
            root.left.val = node_val
            self.values.append(node_val)

        if root.right:
            node_val = 2 * x + 2
            root.right.val = node_val
            self.values.append(node_val)

        self.recover(root.left)
        self.recover(root.right)

        return root

    def traverse(self, root):
        if not root:
            return

        print((root.val))
        self.traverse(root.left)
        self.traverse(root.right)

    def __init__(self, root: TreeNode):
        root.val = 0
        self.values = [0]
        self.root = self.recover(root)


#     def find_target(self,target,root):

#         if not root:
#             return False

#         if root.val == target:
#             return True

#         else:
#             return self.find_target(target,root.left) or self.find_target(target,root.right)


    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
