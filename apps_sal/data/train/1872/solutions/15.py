from collections import defaultdict


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return None

        hashmap = {}
        que = []
        que.append((1, root))

        while len(que) > 0:
            item = que.pop(0)
            depth = item[0]
            node = item[1]
            if depth not in hashmap:
                hashmap[depth] = 0
            hashmap[depth] += node.val

            if node.left is not None:
                que.append((depth + 1, node.left))
            if node.right is not None:
                que.append((depth + 1, node.right))

        sorted_dict = dict(sorted(list(hashmap.items()), key=lambda x: x[1], reverse=True))
        return list(sorted_dict.keys())[0]
