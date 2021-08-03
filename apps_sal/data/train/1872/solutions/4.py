# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # calculate the sum of nodes at each level
        # store the index of the level with max sum until now
        # if two have same, keep the first one, basically only update if its > nonlocal max

        # we can use both dfs and bfs here
        # if we go by bfs, keep calculating sum of level as you add them in the queue
        # tc and sc: O(n) and O(n) for qeuue and traversing

        # if we apply dfs
        # keep a sum hash mapping every level to its total sum, keeping track of max depth encountered until now
        # later we need to traverse this map and find the level with max sum
        # TC: O(n), SC: O(height) for both stack and result map, but height can be O(n in case of skewed trees)
        # lets go with dfs
        # we can actually calc max sum and max depth on the go, to prevent iterating hash later - we cant do it, because suppose a level was max until a point, then a really negative vlaue is encountered at that level, still the max would be that level according to our current logic, which is wrong, we should calc max depth only later

        if not root:
            return 0

        # preorder traversal
        map_depth_sums = collections.defaultdict(int)

        # to avoid sorting of list to find
        max_level = 0
        max_sum = float(-inf)  # since all sums might be negative, we need to find smallest of them all

        # [(5,2)]
        #{1: 1, 2: 10, 3: 10}
        #10, 2
        stack = [(root, 1)]

        while(stack):
            curr_node, level = stack.pop()
            map_depth_sums[level] += curr_node.val

            if curr_node.right:
                stack.append((curr_node.right, level + 1))
            if curr_node.left:
                stack.append((curr_node.left, level + 1))

        level = 1
        while(level in map_depth_sums):
            if map_depth_sums[level] > max_sum:
                max_sum = map_depth_sums[level]
                max_level = level
            level += 1

        return max_level
