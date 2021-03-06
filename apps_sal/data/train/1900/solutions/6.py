class Solution:

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_max_width(root, width, level, d):
            if not root:
                return
            d[level].append(width)
            get_max_width(root.left, 2 * width, level + 1, d)
            get_max_width(root.right, 2 * width + 1, level + 1, d)
        from collections import defaultdict
        d = defaultdict(list)
        get_max_width(root, 0, 0, d)
        print(d)
        max_width = 0
        for (level, elements) in list(d.items()):
            if elements:
                elements.sort()
                curr_width = elements[-1] - elements[0] + 1
                max_width = max(max_width, curr_width)
        return max_width
