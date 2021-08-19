class Stack:

    def __init__(self, stack: list):
        self.stack = stack

    def pop(self):
        if self.stack:
            return self.stack.pop(-1)
        else:
            return None

    def push(self, tree_node: TreeNode):
        self.stack.append(tree_node)


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = Stack([cloned])
        while True:
            node = stack.pop()
            if node is None:
                break
            if node.val == target.val:
                return node
            if not node.right is None:
                stack.push(node.right)
            if not node.left is None:
                stack.push(node.left)
        return None
