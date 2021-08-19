class Solution(object):

    def verticalTraversal(self, root):
        colTable = defaultdict(list)
        (minCol, maxCol) = (0, 0)
        q = [(root, 0, 0)]
        while q:
            (node, x, y) = q.pop()
            if x < minCol:
                minCol = x
            if x > maxCol:
                maxCol = x
            colTable[x].append((-y, node.val))
            if node.left:
                q.append((node.left, x - 1, y - 1))
            if node.right:
                q.append((node.right, x + 1, y - 1))
        return [[x[1] for x in sorted(colTable[col])] for col in range(minCol, maxCol + 1)]
