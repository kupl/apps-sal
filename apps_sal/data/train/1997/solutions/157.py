class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        events = [];
        r = 0;
        
        #collect all events (starts and ends of intervals)
        for i in range(0, len(intervals)):
            events.append([i, intervals[i][0], 0, intervals[i][1]]);
            events.append([i, intervals[i][1], 1, intervals[i][0]]);
        
        #run through each event in order
        events.sort(key=lambda x: (x[1], -x[3]));
        ai = []; #track active intervals
        po = {}; #map each interval to those which could potentially overlap it
        for i in range(0, len(events)):
            #interval beginning
            if events[i][2] == 0:
                po[events[i][0]] = list(ai); #note unterminated intervals, as they may overlap
                ai.append(events[i][0]); #add interval to list of those active
            else: #interval ending
                #if interval not overlapped
                if not list(set(po[events[i][0]]) & set(ai)): #count it
                    r += 1;
                ai.remove(events[i][0]);
                
        return r;
