class Solution:
    def __init__(self):
        self.sols = {}

    def nodes_at_level(self, root, level, target, nodes):
        if root == None:
            return nodes

        if level == target:
            nodes.append(root)
            return nodes

        self.nodes_at_level(root.left, level + 1, target, nodes)
        self.nodes_at_level(root.right, level + 1, target, nodes)

        return nodes

    def sum_at_level(self, root, level, target):
        if root == None:
            return 0

        if level == target:
            return root.val

        result = sum((self.sum_at_level(root.left, level + 1, target), self.sum_at_level(root.right, level + 1, target)))

        return result

    def level_count(self, root):
        if root == None:
            return 0

        if root in self.sols:
            return self.sols[root]

        result = 1 + max(self.level_count(root.left), self.level_count(root.right))

        self.sols[root] = result

        return result

    def all_children(self, nodes):
        for node in nodes:
            if node.left != None:
                yield node.left
            if node.right != None:
                yield node.right

    def maxLevelSum(self, root: TreeNode) -> int:
        levels = [[root]]

        do_more = True
        cur = 1

        max_index = 0
        max_val = sum([x.val for x in levels[-1]])
        while do_more:
            nodes = levels[-1]
            new_nodes = tuple(self.all_children(nodes))
            levels.append(new_nodes)
            do_more = len(new_nodes) > 0

            cur_val = sum([x.val for x in new_nodes])
            if cur_val > max_val:
                max_val = cur_val
                max_index = cur

            cur += 1

        for i, level in enumerate(levels):
            level_sum = sum([x.val for x in level])
            if level_sum > max_val:
                max_index = i
                max_val = level_sum
        return max_index + 1
