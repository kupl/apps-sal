# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.store = self.get_nodes(root)

    def get_nodes(self, root: TreeNode) -> list:
        result = []
        if root is not None:
            start = root
            start.val = 0
            seq = [start]
            while seq:
                store = []
                for i in seq:
                    result.append(i.val)
                    if i.left is not None:
                        left = i.left
                        left.val = i.val * 2 + 1
                        store.append(left)
                    if i.right is not None:
                        right = i.right
                        right.val = i.val * 2 + 2
                        store.append(right)
                seq = store
        return result

    def find(self, target: int) -> bool:
        if target in self.store:
            return True
        else:
            return False
        



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

