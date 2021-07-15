class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        #they're sorted so
        #grab list from A
        #grab list from B
        
        #look for overlap
            #check 
        
        #if B ends before A, then move B along 
        #else move A along
        res = []
        a = 0
        b = 0
        while a < len(A) and b < len(B):
            #check for overlap 
            #interval from further along beginning to backmost back
            start = max(A[a][0], B[b][0])
            end = min(A[a][1], B[b][1])
            
            if start <= end:
                res.append([start,end])
            
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        
        return res
