class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # return self.first_implementation(A, B)
        return self.second_implementation(A, B)
    
    def first_implementation(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        \"\"\"
        Iterate over the two lists with two pointers. If the startpoint of one of the intervals is
        within the end of another then they intersect. On each operation grab the smallest interval
        start point to use as the basis for comparison.
        Time Complexity: O(m + n)
            where m/n are the sizes of the two arrays. since each element is visited at most once.
        Space Complexity: O(1) -- O(n) if taking the output into account
        \"\"\"
        intervals = []
        idx_a = idx_b = 0
        # 1. Find if the intervals intersect by seeing if the interval with the smallest start points end point overlaps with the later one
        def intervals_intersect(interval_a, interval_b):
            # test: [0,2], [1,5] => [1, 2]
            min_inter,max_inter  = (interval_a,interval_b) if interval_a[0] < interval_b[0] else (interval_b,interval_a)
            if min_inter[1] >= max_inter[0]:
                # intervals.append()
                return [max_inter[0], min(max_inter[1], min_inter[1])]
            return None
        
        # 2. iterate over the two interval lists until one of them is exhausted
        while idx_a < len(A) and idx_b < len(B):
            intersection = intervals_intersect(A[idx_a], B[idx_b])
            if intersection:
                intervals.append(intersection)
            # Need to review this discrete math concept.
            # Since all of the intervals are disjoint the smallest end point cannot be joined with another 
            # Test: A ([0,2], [5,10]) -- B ([1,5], [8,12]) produce first intersection [1,2].
            # Given that they're disjoint the next possible interval has to start after the end of the previous. 
            # since A[n][1] < B[m][1] the only next interval could be from A[n+1][0], B[m][0] since B can still encompass other from A's set.
            if A[idx_a][1] < B[idx_b][1]:
                idx_a += 1
            else:
                idx_b += 1

        return intervals
    
    def second_implementation(self,  A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        \"\"\"
        Memoized DP solution offloading the work to a helper function with a bound that returns at the first missed interval
        Time Complexity: O(m+n)
            Each combination will be visited at least once without the bounding function
            The sort at the end accounts for the O(n log n) portion.
        \"\"\"
         # 1. Find if the intervals intersect by seeing if the interval with the smallest start points end point overlaps with the later one
        def intervals_intersect(interval_a, interval_b):
            # test: [0,2], [1,5] => [1, 2]
            min_inter,max_inter  = (interval_a,interval_b) if interval_a[0] < interval_b[0] else (interval_b,interval_a)
            if min_inter[1] >= max_inter[0]:
                return [max_inter[0], min(max_inter[1], min_inter[1])]
            return None 
        
        def find_intersections(idx_a, idx_b):
            if idx_a == len(A) or idx_b == len(B):
                return []
            intervals = []
            interval_a = A[idx_a]
            interval_b = B[idx_b]
            intersection = intervals_intersect(interval_a, interval_b)
            if intersection:
                intervals.append(intersection)
            if interval_a[1] < interval_b[1]:
                idx_a+= 1
            else:
                idx_b += 1
            return intervals + find_intersections(idx_a, idx_b)

        
        return find_intersections(0, 0)
        
        
        
        
