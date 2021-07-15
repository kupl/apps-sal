class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda l:l[0])
        range_list = [item for item in intervals]
        for item in intervals:
            for range_item in range_list:
                a = item[0]
                b = item[1]
                c = range_item[0]
                d = range_item[1]
                if c == a and b == d:
                    break;
                if c <= a and b <= d and item in range_list:
                    range_list.remove(item)
                if a <= c and d <= b:
                    range_list.remove(range_item)
        range_list_2 = range_list
        
    
        print(range_list)
        return len(range_list)
