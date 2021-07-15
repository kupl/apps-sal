class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = list(range(n))
        
        def fixed(i,arr):
            if i!=arr[i]:
                arr[i] = fixed(arr[i],arr)
            return arr[i]
        
        for ty,s,t in edges:
            if ty==3:
                x = fixed(s-1,A)
                y = fixed(t-1,A)
                A[x] = y
        
        both_comps = sum(1 for i in range(n) if A[i] == i)
        
        B = A[:]
        
        for ty, s,t in edges:
            if ty==1:
                x = fixed(s-1,A)
                y = fixed(t-1,A)
                A[x] = y
        
        a_comps = sum(1 for i in range(n) if A[i] == i)

        if a_comps!=1:
            return -1
        
        for ty,s,t in edges:
            if ty==2:
                x = fixed(s-1,B)
                y = fixed(t-1,B)
                B[x] = y
        
        b_comps = sum(1 for i in range(n) if B[i] == i)

        if b_comps!=1:
            return -1
        
        return len(edges) - (n-a_comps-b_comps+both_comps)
