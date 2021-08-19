# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nMap = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        xMin, xMax = 0, 0
        while queue:
            tmp = collections.defaultdict(list)
            for i in range(len(queue)):
                node, nX = queue.popleft()
                tmp[nX].append(node.val)
                if node.left:
                    queue.append((node.left, nX - 1))
                    xMin = min(xMin, nX - 1)
                if node.right:
                    queue.append((node.right, nX + 1))
                    xMax = max(xMax, nX + 1)
            for i in tmp:
                nMap[i] += sorted(tmp[i])
        traversalLst = []
        return [nMap[i] for i in range(xMin, xMax + 1)]
