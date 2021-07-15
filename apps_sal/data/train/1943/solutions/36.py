class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        \"\"\"
        each lists are pairwise disjoint and in sorted order based on what, length? no, start!
        return the intersection of two lists
        
        [1,2], [5,5], [8,10], [15, 23], [24,24], [25, 25]
        runtime -- O(n+m)
        space comp. -- O(n+m)
        \"\"\"
        commonRegion= []
        ptr1, ptr2=0, 0
        while ptr1 <len(A) and ptr2< len(B):
            if self.isCommon(A[ptr1], B[ptr2]):
                newInterval= max(A[ptr1][0], B[ptr2][0]), min(A[ptr1][1], B[ptr2][1])
                commonRegion.append(newInterval)
            if A[ptr1][1] >= B[ptr2][1]:
                ptr2+=1
            else:
                ptr1+=1
        return commonRegion
    
    def isCommon(self, x, y):
        a, b= sorted([x, y], key= lambda x:x[0]) # sort based on starting 
        return a[1]>= b[0]
