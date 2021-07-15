class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A, B, n = [], [], len(costs) // 2 # person id list
        diff = []
        for i, (a, b) in enumerate(costs):
            diff.append((i, (a - b)))
            if a < b:
                A.append(i)
            else:
                B.append(i)
            
        
        # print(diff)
        # new_A, new_B = [], []
        # diff_num = abs(len(A)-len(B))
        flag = 0
        if len(A) > len(B): # 飞到A的多, 把diff<0且值较小的A放到B, 
            flag = 1
            # 从大到小排序
            diff = sorted(diff, key = lambda x: x[1], reverse=True)
            for i, x in diff:
                if x > 0 or i in B:
                    continue
                B.append(i)
                if len(B) == n:
                    break
            
        elif len(A) < len(B): # 飞到B的多, 把diff>0且值较小的B放到A
            # new_A = A
            flag = 2
            # 从小到大排序
            diff = sorted(diff, key = lambda x: x[1])
            
            for i, x in diff:
                if i in A: continue
                A.append(i)
                if len(A) == n:
                    break
            
        # print(flag, A, B)
        res = 0
        for i in range(2 * n):
            a, b = costs[i]
            if flag == 1:
                res += b if i in B else a
                  
            if flag == 2 or flag == 0:
                res += a if i in A else b                        
      
        return res
            
            
            
            
            
# [1,2], [2,3] ,[3,5],[4,5]
       
# 1 -> A 10
# 2 -> A 30
# 3 -> B 50
# 4 -> B 20

# # A = [10,30]
# # B = [20,200]


# 1 -> A 259


# 2 -> B 54 -54 + 448 = 394
# 3 -> B 667 -667 + 926 = 259 
# 4 -> B 139 - 139 + 184 = 45 -> A
# 5 -> B 118 - 118 + 840 = 772
# 6 -> B 469 - 469 + 577 = 108

# A = [259, 184, 577]
# B = [54， 667， 118]


# min(sum(A) + sum(B)) s.t. len(A) == len(B)




