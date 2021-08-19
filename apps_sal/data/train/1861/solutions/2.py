class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        # count of each distinct x axis point
        countx = len(set(x for x, y in points))
        # count of each distinct y axixs point
        county = len(set(y for x, y in points))

        # if either same as n, no points for that axis
        if countx == n or county == n:
            return 0

        container = defaultdict(list)

        # add y val to x list in container if x > y, opposite if otherwise
        if countx > county:
            for x, y in points:
                container[x].append(y)
        else:
            for x, y in points:
                container[y].append(x)

        # seen set/dict
        lastx = {}
        ans = float('inf')

        for x in sorted(container):
            container[x].sort()
            # loop for the len of x's list in container
            for y in range(len(container[x])):
                # loop curr num/index
                for z in range(y):
                    # get from container
                    y1, y2 = container[x][z], container[x][y]

                    # seen before, reset ans to min of itself and last seen x, curr y
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * abs(y2 - y1))
                    # put curr x in seen
                    lastx[y1, y2] = x

        return ans if ans < float('inf') else 0
