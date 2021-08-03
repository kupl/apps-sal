# This is a really difficult problem, method is called line sweeping, it also has interval merge in it
# 1. Time complexity O(N*N*log(N)), space complexity O(N)
# 2. Idea is to use a vertical line to sweep from left to right and accumulate the area by delta x times the total interval length at the x position
# class Solution(object):
#     def rectangleArea(self, rectangles):
#         M=10**9+7
#         events=[]
#         for x1,y1,x2,y2 in rectangles:
#             events.append((x1,y1,y2,0))
#             events.append((x2,y1,y2,1))
#         events.sort(key=lambda x:x[0])
#         res=0
#         prev=events[0][0]
#         actives=[]
#         def getWidth(actives):
#             actives.sort(key=lambda x:x[0])
#             width=0
#             right=0
#             for active in actives:
#                 width+=max(0,active[1]-max(right,active[0]))
#                 right=max(right,active[1])
#             return width
#         for event in events:
#             if event[0]!=prev:
#                 res+=getWidth(actives)*(event[0]-prev)
#                 res=res%M
#                 prev=event[0]
#             if not event[3]:
#                 actives.append(event[1:-1])
#             else:
#                 actives.remove(event[1:-1])
#         return res

# This second solution is a practice of segmentation tree, the concept is simpmle but implementation is very challenging, with segmentation tree, each update take log(N) time so time complexity of the enti

class Tree:
    def __init__(self, l, r):
        self.total = 0
        self.count = 0
        self.l = l
        self.r = r
        self.m = int((self.l + self.r) / 2)
        self.isLeaf = True if self.r - self.l == 1 else False
        self.left = None if self.isLeaf else Tree(self.l, self.m)
        self.right = None if self.isLeaf else Tree(self.m, self.r)

    def update(self, l, r, count):
        if l >= self.r or r <= self.l:
            return
        if self.isLeaf:
            self.count += count
            self.total = nums[self.r] - nums[self.l] if self.count else 0
        else:
            self.left.update(l, r, count)
            self.right.update(l, r, count)
            self.total = self.left.total + self.right.total


class Solution(object):
    def rectangleArea(self, rectangles):
        M = 10**9 + 7
        events = []
        nonlocal nums
        nums = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))
            events.append((x2, y1, y2, -1))
            nums.add(y1)
            nums.add(y2)
        nums = list(nums)
        nums.sort()
        nToI = dict([(n, i) for i, n in enumerate(nums)])
        iTree = Tree(0, len(nums) - 1)
        events.sort(key=lambda x: x[0])
        res = 0
        prev = events[0][0]
        for event in events:
            if event[0] != prev:
                res += iTree.total * (event[0] - prev)
                res = res % M
                prev = event[0]
            iTree.update(nToI[event[1]], nToI[event[2]], event[3])
        return res
