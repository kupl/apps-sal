# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.tree = root
        self.values = []
        from collections import deque
        stack = deque()
        stack.append(root)
        root.val = 0
        curr = root
        while stack:
            if curr:
                self.values.append(curr.val)
                if curr.left:
                    curr.left.val = 2 * curr.val + 1
                if curr.right:
                    curr.right.val = 2 * curr.val + 2
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

    def find(self, target: int) -> bool:
        if target in self.values:
            return True
        else:
            return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

