# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.val_list = []
        def construct(node, val):
            if not node:
                return None
            node.val = val
            self.val_list.append(val)
            node.left = construct(node.left, 2*val+1)
            node.right = construct(node.right, 2*val+2)
            return node
        self.root = construct(root, 0)
        

    def find(self, target: int) -> bool:
        '''
        root = self.root
        def traverse(node):
            if not node:
                return False
            if node.val == target:
                return True
            elif target < node.val:
                return False
            else:
                return traverse(node.left) or traverse(node.right)
        return traverse(root)
        '''
        return target in self.val_list


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

