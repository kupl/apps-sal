# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        hmap = defaultdict(list)
        x_min, x_max = 0, 0
        queue = deque()
        report = list()
        if root:
            queue.append((root, 0, 1))
        else:
            return report
        
        while queue:
            root, x, y = queue.popleft()
            
            x_min = min(x, x_min)
            x_max = max(x, x_max)
            while y > len(hmap[x]):
                hmap[x].append([])
            hmap[x][-1].append(root.val)
                
            if root.left:
                queue.append((root.left, x - 1, y + 1))
            if root.right:
                queue.append((root.right, x + 1, y + 1))
                
        print(hmap) 
        print(x_min, x_max)
        for i in range(x_min, x_max + 1):
            report.append([])
            for l in hmap[i]:
                print(l)
                print(report)
                if l:
                    l.sort()
                    report[-1].extend(l)
        return report
