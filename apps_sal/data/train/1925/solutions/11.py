class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(val=preorder[0])
        parents = [(root.val, root)]
        heapq.heapify(parents)
        for idx in range(1, len(preorder)):
            num = preorder[idx]
            node = TreeNode(val=num)
            tmp = None
            while parents and parents[0][0] < num:
                (_, tmp) = heapq.heappop(parents)
            if tmp:
                tmp.right = node
            elif not tmp and parents:
                parents[0][1].left = node
            heapq.heappush(parents, (num, node))
        return root
