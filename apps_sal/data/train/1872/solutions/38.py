class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        maximum = root.val
        maximum_level = 1
        cnt = 1
        while queue:
            summation = 0
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                summation += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if summation > maximum:
                maximum = summation
                maximum_level = cnt
            cnt += 1
        return maximum_level
