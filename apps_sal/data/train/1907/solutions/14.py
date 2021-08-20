class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = []

        def traverse(x):
            if not x:
                return False
            if x is target:
                return True
            if traverse(x.left):
                path.append(True)
                return True
            if traverse(x.right):
                path.append(False)
                return True
            return False
        traverse(original)
        pointer = cloned
        for x in reversed(path):
            if x:
                pointer = pointer.left
            else:
                pointer = pointer.right
        return pointer
