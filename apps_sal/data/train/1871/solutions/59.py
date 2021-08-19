import queue
from collections import defaultdict


class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxDiff = 0
        dq = queue.deque()
        dq.append(root)
        data = []
        nodes = defaultdict(list)
        while any(dq):
            node = dq.popleft()
            data.append(node.val)
            if node.left:
                dq.append(node.left)
                nodes[node.left.val].append(node.val)
                nodes[node.left.val].extend(nodes[node.val])
            if node.right:
                dq.append(node.right)
                nodes[node.right.val].append(node.val)
                nodes[node.right.val].extend(nodes[node.val])
        for (key, value) in list(nodes.items()):
            if not value:
                continue
            s = 0
            for val in value:
                if abs(key - val) > s:
                    s = abs(key - val)
            if s > maxDiff:
                maxDiff = s
        return maxDiff
