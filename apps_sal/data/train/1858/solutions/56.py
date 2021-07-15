# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recover(root, nodes):
    nodes.append(root.val)
    if root.left:
        root.left.val = 2*(root.val) + 1
        recover(root.left, nodes)
    if root.right:
        root.right.val = 2*(root.val) + 2
        recover(root.right, nodes)
    
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        nodes = []
        recover(root, nodes)
        self.tree = root
        self.nodes = nodes

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

