class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        accs = []
        
        for i in range(n):
            acc = [0]
            
            for j in range(m):
                acc.append(acc[-1]+mat[i][j])
            
            accs.append(acc)
        
        ans = 0
        
        for i in range(m):
            for j in range(i, m):
                cnt = 0
                
                for k in range(n):
                    if accs[k][j+1]-accs[k][i]==j-i+1:
                        cnt += 1
                    else:
                        ans += cnt*(cnt+1)//2
                        cnt = 0
        
                ans += cnt*(cnt+1)//2
        
        return ans
