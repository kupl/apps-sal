class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        max_zigzag = 0
        zigzag = 0
        stack = [(root, None, 0)]
        while stack:
            node = stack[-1][0]
            prev_dir = stack[-1][1]
            max_up_to_node = stack[-1][2]
            del stack[-1]
            if max_up_to_node > max_zigzag:
                max_zigzag = max_up_to_node
            if prev_dir == None:
                if node.right != None:
                    stack.append((node.right, 'R', max_up_to_node + 1))
                if node.left != None:
                    stack.append((node.left, 'L', max_up_to_node + 1))
            else:
                if prev_dir == 'R':
                    if node.right != None:
                        stack.append((node.right, 'R', 1))
                    if node.left != None:
                        stack.append((node.left, 'L', max_up_to_node + 1))
                if prev_dir == 'L':
                    if node.right != None:
                        stack.append((node.right, 'R', max_up_to_node + 1))
                    if node.left != None:
                        stack.append((node.left, 'L', 1))
        return max_zigzag
