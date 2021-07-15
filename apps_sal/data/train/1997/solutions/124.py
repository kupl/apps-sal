class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c=0
        if len(intervals)==1:
            return 1
        else:
            for i in range(len(intervals)):
                print(\"i\")
                print(i)
                for j in range(len(intervals)):
                    print(\"j\")
                    print(j)
                    if i!=j and intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1]:
                        c+=1
                        break
            return len(intervals)-c
                         
