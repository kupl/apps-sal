class Solution:
#    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # Populate events
#         OPEN, CLOSE = 0, 1
#         events = []
#         for x1, y1, x2, y2 in rectangles:
#             events.append((y1, OPEN, x1, x2))
#             events.append((y2, CLOSE, x1, x2))
#         events.sort()

#         def query():
#             ans = 0
#             cur = -1
#             for x1, x2 in active:
#                 cur = max(cur, x1)
#                 ans += max(0, x2 - cur)
#                 cur = max(cur, x2)
#             return ans

#         active = []
#         cur_y = events[0][0]
#         ans = 0
#         for y, typ, x1, x2 in events:
#             # For all vertical ground covered, update answer
#             ans += query() * (y - cur_y)

#             # Update active intervals
#             if typ is OPEN:
#                 active.append((x1, x2))
#                 active.sort()
#             else:    
#                 active.remove((x1, x2))

#             cur_y = y

#         return ans % (10**9 + 7)
    
#         OPEN, CLOSE = 0,1
#         events = []
#         for x1, y1, x2, y2 in rectangles:
#             events.append((y1, OPEN, x1, x2))
#             events.append((y2, CLOSE, x1, x2))
        
#         events.sort()
        
#         # total length of the horizontal intervals
#         def query():
#             ans = 0
#             cur = -1
#             for x1, x2 in active:
#                 cur = max(cur, x1)
#                 ans += max(0, x2-cur)
#                 cur = max(cur, x2)
#             return ans
            
#         active = []
#         cur_y = events[0][0]
#         res = 0
#         for y, typ, x1, x2 in events:
#             res += query()*(y - cur_y)
            
#             if typ is OPEN:
#                 active.append((x1, x2))
#                 active.sort()
#             else:
#                 active.remove((x1,x2))
            
#             cur_y = y
            
#         return res % (10**9 + 7)
    def rectangleArea(self, rectangles):
        OPEN, CLOSE = 1, -1
        events = []
        nonlocal X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X.add(x1)
            X.add(x2)
        events.sort()

        X = sorted(X)
        Xi = {x: i for i, x in enumerate(X)}

        active = Node(0, len(X) - 1)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(Xi[x1], Xi[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)
    
class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, i, j, val):
        if i >= j: return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total

