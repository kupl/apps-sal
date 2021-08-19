class Solution:

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        queue = []
        queue.append([0, root])
        while len(queue) != 0:
            (level, temp) = queue.pop(0)
            if len(result) < level + 1:
                result.append([])
            if level % 2 == 0:
                result[level].append(temp.val)
            else:
                result[level].insert(0, temp.val)
            if temp.left:
                queue.append([level + 1, temp.left])
            if temp.right:
                queue.append([level + 1, temp.right])
        return result
