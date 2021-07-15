# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.q = []
        def search(node, value):
            if node:
                self.q.append(value)
                search(node.left, value*2 + 1)
                search(node.right, value*2 + 2)
        search(root,0)
        

    def find(self, target: int) -> bool:
        return target in self.q


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

