class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.idxes = collections.defaultdict(list)
        for (i, n) in enumerate(arr):
            self.idxes[n].append(i)
        self.arr = arr
        self.st = SegmentTree(len(arr), arr, self.idxes)

    def query(self, left: int, right: int, threshold: int) -> int:
        maj = self.st.query_maj(left, right)
        if maj:
            l, r = bisect.bisect_left(self.idxes[maj], left), bisect.bisect(self.idxes[maj], right)
            if r - l >= threshold:
                return maj
        return -1

class SegmentTree:
    
    def __init__(self, n, arr, idxes):
        self.root = Node(0, n - 1, arr, idxes)
        
    def query_maj(self, lo, hi):
        return self.root.query_maj(lo, hi)

class Node:
    
    def __init__(self, lo, hi, arr, idxes):
        self.lo, self.hi = lo, hi
        self.lc, self.rc = None, None
        self.arr, self.idxes = arr, idxes
        self.maj = None
        
    def query_maj(self, lo, hi):
        
        def is_maj(n):
            if not n:
                return False
            
            l = bisect.bisect_left(self.idxes[n], lo)
            r = bisect.bisect(self.idxes[n], hi)
            return (r - l << 1) > hi - lo
        
        if lo > hi or self.lo > hi or self.hi < lo:
            return None
        
        if self.lo >= lo and self.hi <= hi:
            if not self.maj:
                if self.lo == self.hi:
                    self.maj = self.arr[self.lo]
                else:
                    mi = (self.lo + self.hi) >> 1
                    if not self.lc:
                        self.lc = Node(self.lo, mi, self.arr, self.idxes)
                    if not self.rc:
                        self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
                    l = self.lc.query_maj(self.lo, mi)
                    r = self.rc.query_maj(mi + 1, self.hi)
                    self.maj = l if is_maj(l) else r if is_maj(r) else -1
            return self.maj
        
        mi = (self.lo + self.hi) >> 1
        if not self.lc:
            self.lc = Node(self.lo, mi, self.arr, self.idxes)
        if not self.rc:
            self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
    
        l = self.lc.query_maj(lo, hi)
        r = self.rc.query_maj(lo, hi)
        return l if is_maj(l) else r if is_maj(r) else -1
        
#         def is_maj(n):
#             if not n:
#                 return False
            
#             l = bisect.bisect_left(self.idxes[n], lo)
#             r = bisect.bisect(self.idxes[n], hi)
#             return (r - l << 1) > hi - lo
        
#         def get_children_maj():
#             l, r = None, None
#             mi = (self.lo + self.hi) >> 1
#             # if lo <= mi:
#             if not self.lc:
#                 self.lc = Node(self.lo, mi, self.arr, self.idxes)
#             l = self.lc.query_maj(lo, hi)
            
#             # if mi + 1 <= hi:
#             if not self.rc:
#                 self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
#             r = self.rc.query_maj(lo, hi)
            
#             return l, r
        
#         if self.lo > hi or self.hi < lo:
#             return None
#         if self.lo == self.hi:
#             return self.arr[self.lo]
        
#         if lo <= self.lo <= self.hi <= hi:
#             # lazy population: initially, 'self.maj' is not set
#             if not self.maj:
#                 # base case: only 1 element in the node
#                 # and that must be the majority element
#                 # if self.lo == self.hi:
#                 #     self.maj = self.arr[self.lo]
#                 # else:
#                     # l, r = get_children_maj()
                    
                    
#                 mi = (self.lo + self.hi) >> 1
#                 # if lo <= mi:
#                 if not self.lc:
#                     self.lc = Node(self.lo, mi, self.arr, self.idxes)
#                 l = self.lc.query_maj(lo, hi)

#                 # if mi + 1 <= hi:
#                 if not self.rc:
#                     self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
#                 r = self.rc.query_maj(lo, hi)


#                 if is_maj(l):
#                     self.maj = l
#                 elif is_maj(r):
#                     self.maj = r
#                 else:
#                     self.maj = -1
#             return self.maj
        
#         # l, r = get_children_maj()
#         # return l if is_maj(l) else r if is_maj(r) else None
#         mi = (self.lo + self.hi) >> 1
#         # if lo <= mi:
#         if not self.lc:
#             self.lc = Node(self.lo, mi, self.arr, self.idxes)
#         l = self.lc.query_maj(lo, hi)

#         # if mi + 1 <= hi:
#         if not self.rc:
#             self.rc = Node(mi + 1, self.hi, self.arr, self.idxes)
#         r = self.rc.query_maj(lo, hi)
#         if is_maj(l):
#             return l
#         if is_maj(r):
#             return r
#         return -1




# class Node:
    
#     def __init__(self, lo, hi, arr, cnt):
#         self.lo, self.hi = lo, hi
#         # self.maj: the majority element in range [self.lo, self.hi]
#         self.left, self.right, self.maj = None, None, None
#         self.arr, self.cnt = arr, cnt
    
#     def query(self, lo, hi):
        
#         def isMaj(n):
#             if n:
#                 l, r = bisect.bisect_left(self.cnt[n], lo), bisect.bisect_right(self.cnt[n], hi)
#                 return (r - l) * 2 > hi - lo
#             return False
        
#         if lo > hi or self.lo > hi or self.hi < lo:
#             return None
#         if self.lo == self.hi:
#             return self.arr[self.lo]
        
#         if self.lo >= lo and self.hi <= hi:
#             if not self.maj:
#                 mi = (self.lo + self.hi) >> 1
#                 if not self.left:
#                     self.left = Node(self.lo, mi, self.arr, self.cnt)
#                 if not self.right:
#                     self.right = Node(mi + 1, self.hi, self.arr, self.cnt)
#                 l = self.left.query(self.lo, mi)
#                 r = self.right.query(mi + 1, self.hi)
#                 if l != -1 and isMaj(l):
#                     self.maj = l
#                 elif r != -1 and isMaj(r):
#                     self.maj = r
#                 else:
#                     self.maj = -1
#             return self.maj
        
#         mi = (self.lo + self.hi) >> 1
#         if not self.left:
#             self.left = Node(self.lo, mi, self.arr, self.cnt)
#         if not self.right:
#             self.right = Node(mi + 1, self.hi, self.arr, self.cnt)
    
#         l = self.left.query(lo, hi)
#         r = self.right.query(lo, hi)
#         if l != -1 and isMaj(l):
#             return l
#         if r != -1 and isMaj(r):
#             return r
#         return -1

# class MajorityChecker:

#     def __init__(self, arr: List[int]):
#         self.cnt = collections.defaultdict(list)
#         for (i, v) in enumerate(arr):
#             self.cnt[v] += i,
#         self.arr = arr
#         self.root = Node(0, len(arr) - 1, self.arr, self.cnt)
    
#     def query(self, left: int, right: int, threshold: int) -> int:
#         elm = self.root.query(left, right)
#         if elm != -1:
#             lo, hi = bisect.bisect_left(self.cnt[elm], left), bisect.bisect_right(self.cnt[elm], right)
#             if hi - lo >= threshold:
#                 return elm
#         return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

