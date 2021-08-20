class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:

        def countNodes(node):
            left = 0
            if node == None:
                return 0
            if node.left:
                left = countNodes(node.left)
            right = 0
            if node.right:
                right = countNodes(node.right)
            return left + right + 1

        def searchNode(node, x):
            if node.val == x:
                return node
            if node.left:
                tmp = searchNode(node.left, x)
                if tmp:
                    return tmp
            if node.right:
                tmp = searchNode(node.right, x)
                if tmp:
                    return tmp
            return None
        node = searchNode(root, x)
        left = countNodes(node.left)
        right = countNodes(node.right)
        parent = n - left - right - 1
        if parent > n - parent or left > n - left or right > n - right:
            return True
        return False
