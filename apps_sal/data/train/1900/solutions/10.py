class Solution:

    def isInt(self, e):
        return type(e).__name__ == 'int'

    def testNode(self, node, newStack):
        acc = 0
        if node:
            newStack.append(node)
            acc += 1
        elif len(newStack):
            acc += 1
            if self.isInt(newStack[-1]):
                newStack[-1] += 1
            else:
                newStack.append(1)
        return acc

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        res = 1
        while len(stack):
            newStack = []
            acc = 0
            for node in stack:
                if self.isInt(node):
                    if len(newStack):
                        if self.isInt(newStack[-1]):
                            newStack[-1] += 2 * node
                        else:
                            newStack.append(2 * node)
                        acc += 2 * node
                else:
                    acc += self.testNode(node.left, newStack)
                    acc += self.testNode(node.right, newStack)
            stack = newStack
            if len(newStack) and self.isInt(newStack[-1]):
                acc -= stack.pop()
            res = max(res, acc)
        return res
