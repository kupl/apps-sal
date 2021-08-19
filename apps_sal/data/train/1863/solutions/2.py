# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        XYAndNode = namedtuple('XYAndNode', ('x', 'y', 'node'))

        q = deque([XYAndNode(0, 0, root)])
        group_by_x = defaultdict(list)
        min_x = max_x = 0

        while q:
            x, y, node = q.popleft()
            group_by_x[x].append((y, node.val))
            min_x = min(min_x, x)
            max_x = max(max_x, x)

            if node.left:
                q.append(XYAndNode(x - 1, y + 1, node.left))
            if node.right:
                q.append(XYAndNode(x + 1, y + 1, node.right))

        output = []
        for x in range(min_x, max_x + 1):
            column = [i[1] for i in sorted(group_by_x[x])]
            output.append(column)

        return output
