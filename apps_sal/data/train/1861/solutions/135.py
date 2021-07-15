class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)   # this is my 1st thought, should be a dictionary of lists. 
    # Here is the right way to define the dictionary.
    # This is one of the KEY step shorten the time. If define in the opposite way, short dictionary but long lists, ~5 fold slower.
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)  # if using this define, long dictionary, each list is short.

        lastx = {}
        res = float('inf')

        for x in sorted(p):
            p[x].sort() # the dictionary p and the list in p must be sorted here, because it was unknown x or y should be the keys for the dictionary. 
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i] # fix one dimension, find possible pairs for the other dimention.
                    #Record the fixed dimension as value, the pair as the key.
                    if (y1, y2) in lastx:  
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1)) # if the pari appeared before, calculate an area, compare with the current min.
                    lastx[y1, y2] = x # no matter the pair appeared before or not, record the new one. 
                    # This is because the dictionary is sorted, the last must be the lowest.
        return res if res < float('inf') else 0  # simple version.

