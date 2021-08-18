class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:

        def helper(current_depth, s):
            split_point1 = -1
            split_point2 = -1
            next_depth = current_depth + 1
            count = 0
            whole_count = 0
            for index, c in enumerate(s):
                if c == '-':
                    whole_count += 1
                    count += 1
                else:
                    if count == next_depth:
                        if split_point1 == -1:
                            split_point1 = index
                        else:
                            split_point2 = index
                    count = 0
            if whole_count == 0:
                return TreeNode(int(s))
            else:
                root = TreeNode(int(s[:split_point1 - next_depth]))

                if split_point2 != -1:
                    root.left = helper(next_depth, s[split_point1:split_point2 - next_depth])
                    root.right = helper(next_depth, s[split_point2:])
                else:
                    root.left = helper(next_depth, s[split_point1:])
                    root.right = None
            return root
        return helper(0, S)
