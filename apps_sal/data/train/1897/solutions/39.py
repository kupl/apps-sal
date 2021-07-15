class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        def constSeg(tree, n, arr):
            tree[n:] = arr
            
            for i in range(n-1,0,-1):
                tree[i] = tree[2*i] ^ tree[2*i+1]
        
        def getQuery(beg, end):
            beg += n
            end += n
            
            ans = 0
            
            while(beg<end):
                if beg&1:
                    ans ^= tree[beg]
                    beg += 1
                if end&1:
                    end -= 1
                    ans ^= tree[end]
                
                beg //= 2
                end //=2
            
            return ans
                    
        n = len(arr)
        tree = [0]*(2*len(arr))
        constSeg(tree,len(arr),arr)
        
        ans = []
        for i in queries:
            ans.append(getQuery(i[0], i[1]+1))
        
        return ans
            
        

