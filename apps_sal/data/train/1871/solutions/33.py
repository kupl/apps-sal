# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        \"\"\"
        IDEA: 每條path時拉出max_diff，打擂台!
        1. max_diff 查法複雜度分析：
            a. 對於一條path，最糟拉成一條:5000 * 5000 + 5000，貌似可行
                    ==> O(N^2)
            b. 優化：當path上那一顆大於我，就讓它作為 ref_value 去跟再後面的相剪
                    ==> O(N)
        \"\"\"
        \"\"\"
        ISSUES:
        1. [0,null,1], 我覺得該是 0, 但answer說是1,
            Sol, WRONG: 葉節點時，葉子自己的值也放入打擂台 X
            Sol, calc_max_diff 中，先計算diff後，如果j指的地方比i大，再把i指到j上面去
        \"\"\"
        
        if not root:
            return 0
        max_diff = [0]  # [max, min]
        # self.helper(root, [], max_diff)
        self.helper_early_return(root, [], max_diff)
        return max(max_diff[0], 0)  # 避免所有的祖先都比子孫們都小
    
        min_max = [root.val, root.val]
        self.helper2_FAILED(root, [], max_diff, min_max)   # WRONG! 同步存儲 min_max，FAILED... 因為backtrack時得把那條路徑所貢獻的min或max放回去… 多事又麻煩
        # return res[0] - res[1]
        return min_max[1] - min_max[0]

    def helper2_FAILED(self, root, items, max_diff, min_max): # min_max at the same time
        if not root:
            # return
            # if not root.left and not root.right:
            cur_max_diff = min_max[1] - min_max[0]
            print(items, min_max)
            max_diff[0] = max(cur_max_diff, max_diff[0])
            return 
        min_max[0], min_max[1] = min(min_max[0], root.val), max(min_max[1], root.val)
        self.helper2(root.left, items + [root.val], max_diff, min_max)
        self.helper2(root.right, items + [root.val], max_diff, min_max)
    
    
    def helper(self, root, items, max_diff):
        if not root:
            cur_max_diff = self.calc_max_diff(items)
            max_diff[0] = max(cur_max_diff, max_diff[0])
            return 
            
        self.helper(root.left, items + [root.val], max_diff)
        self.helper(root.right, items + [root.val], max_diff)
    
    def helper_early_return(self, root, items, max_diff):
        if not root:
            return
        if not root.left and not root.right:
            cur_max_diff = self.calc_max_diff(items + [root.val])
            max_diff[0] = max(cur_max_diff, max_diff[0])
            return 
            
        self.helper_early_return(root.left, items + [root.val], max_diff)
        self.helper_early_return(root.right, items + [root.val], max_diff)
        
    def calc_max_diff(self, items):
        \"\"\" 8 3 6 7 
            i j
        \"\"\"
        n = len(items)
        # print(items)
        i = 0
        \"\"\" O(N) Optimization in calc_max_diff! \"\"\"
        cur_max = cur_min = items[0]
        for i in range(n):
            cur_max = max(cur_max, items[i])
            cur_min = min(cur_min, items[i])
        return cur_max-cur_min
    
        \"\"\" Orig O(N^2) calc_max_diff \"\"\"
        cur_max_diff = 0
        while i < n:
            for j in range(i+1, n):
                diff = abs(items[i] - items[j])
                cur_max_diff = max(diff, cur_max_diff)
            i += 1
        return cur_max_diff
    
#     def calc_max_diff_WRONG(self, items):   # 這是要求parent必比較大時的優化
#         \"\"\" 8 3 6 7 
#             i j
#         \"\"\"
        
#         n = len(items)
#         print(items)
#         i = 0
#         cur_max_diff = 0
#         while i < n:
#             for j in range(i+1, n):
#                 diff = items[i] - items[j]
#                 cur_max_diff = max(diff, cur_max_diff)
#                 if items[j] > items[i]:
#                     i = j
#                     # break
#                     continue

#             i += 1
#         return cur_max_diff
