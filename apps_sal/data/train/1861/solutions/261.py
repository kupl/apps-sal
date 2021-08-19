class Solution(object):
    def minAreaRect(self, points):
        # idea, use lookup set to store the point that has seen before. for (x1,y1) in points, for (x2,y2) in lookup, check whether (x1,y2) and (x2, y1) in lookup. Time O(n^2), Space O(n).
        res = float('inf')  # initiate as inf
        lookup = set()
        for x1, y1 in points:
            for x2, y2 in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:  # if all in the lookup
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))  # check the min area
            # add to lookup for the outer loop
            lookup.add((x1, y1))
        return res if res != float('inf') else 0
