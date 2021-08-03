# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #         def traverse(node: TreeNode, good_threshold: int) -> int:
        #             good_threshold = max(good_threshold, node.val)

        #             left_count = right_count = 0

        #             if node.left is not None:
        #                 left_count = traverse(node.left, good_threshold)

        #             if node.right is not None:
        #                 right_count = traverse(node.right, good_threshold)

        #             return left_count + right_count + (1 if good_threshold <= node.val else 0)

        #         good_count = traverse(root, -10e4)

        #         return good_count
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
