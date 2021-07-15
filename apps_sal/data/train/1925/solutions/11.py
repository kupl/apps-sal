# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # 
        # minHeap | O(NlogN) | ----- 40 ms (50.65%) / 14.3 MB (5.13%)
        # ------------------------------------------------------------------------------------------------
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
                _, tmp = heapq.heappop(parents)
            if tmp:
                tmp.right = node
            elif not tmp and parents:
                parents[0][1].left = node
            heapq.heappush(parents, (num, node))   
        return root
