class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([[root, 0]])
        ret = 0
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node, pos = queue.pop()
                level.append(pos)
                if node.left:
                    queue.appendleft([node.left, pos * 2])
                if node.right:
                    queue.appendleft([node.right, 1 + pos * 2])
            print(level)
            ret = max(ret, level[-1] - level[0] + 1)
        return ret
