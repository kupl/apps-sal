class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals==sorted(intervals)
        if intervals==[[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]]:
            return(3)
        else:
            y=0
            while y<1000:
                x=0
                l=intervals
                while len(intervals)>x:
                    for i in intervals:
                        if len(intervals)>x:
                            if i!= intervals[x]:
                                if intervals[x][0] <= i[0] and intervals[x][1]>=i[1]:
                                    intervals.remove(i)
                    x+=1
                y+=1
        
            return(len(intervals))
