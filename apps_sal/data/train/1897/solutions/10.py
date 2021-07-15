class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len(arr)==1:
            return [arr[0] for i in queries]
        
        table = [arr[0]]*len(arr)
        for i in range(1,len(arr)):
            table[i] = table[i-1] ^ arr[i] 
        '''
        print(table)
        print(arr[0])
        print(arr[0]^arr[1])
        print(arr[0]^arr[1]^arr[2])
        print(arr[0]^arr[1]^arr[2]^arr[3
        '''
        
        '''
        table = [out]*len(arr)
        for i in range(1,len(arr)):
            for j in range(i,len(arr)):
                table[i][j] = table[i-1][j] ^ arr[j]
        '''
        out = [0]*len(queries)
        for i,(l,r) in enumerate(queries):
            #print(f'i:{i}, l:{l}, r:{r}')
            if l>0:
                out[i] = table[l-1] ^ table[r] 
            else:
                out[i] = table[r]
            
        return out
