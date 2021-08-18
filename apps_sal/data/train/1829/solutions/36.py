class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        queue = deque()
        TraverseItem = namedtuple('TraverseItem', ['threshold', 'node'])
        queue.append(TraverseItem(threshold=-10e4, node=root))

        good_count = 0

        while len(queue) != 0:
            n = queue.pop()

            threshold = max(n.node.val, n.threshold)

            if n.node.left is not None:
                queue.append(TraverseItem(threshold=threshold, node=n.node.left))

            if n.node.right is not None:
                queue.append(TraverseItem(threshold=threshold, node=n.node.right))

            if threshold <= n.node.val:
                good_count = good_count + 1

        return good_count
