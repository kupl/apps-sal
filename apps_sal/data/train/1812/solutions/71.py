class MajorityChecker:

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.a, self.a2i = A, a2i

    def query(self, left: int, right: int, threshold: int) -> int:

        track = self.a2i

        l, r = left, right

        if((r - l + 1) % 2 == 0):
            mid = l - 1 + (r - l + 1) // 2

        else:
            mid = l + (r - l + 1) // 2

        if((r - mid + 1) % 2 == 0):
            mid1 = mid - 1 + (r - mid + 1) // 2

        else:
            mid1 = mid + (r - mid + 1) // 2

        if((mid - l + 1) % 2 == 0):
            mid2 = l - 1 + (mid - l + 1) // 2

        else:
            mid2 = l + (mid - l + 1) // 2

        t1 = bisect.bisect_left(track[self.a[mid]], left)
        t2 = bisect.bisect_right(track[self.a[mid]], right)

        if(t2 - t1 >= threshold):
            return self.a[mid]

        t1 = bisect.bisect_left(track[self.a[mid1]], left)
        t2 = bisect.bisect_right(track[self.a[mid1]], right)

        if(t2 - t1 >= threshold):
            return self.a[mid1]

        t1 = bisect.bisect_left(track[self.a[mid2]], left)
        t2 = bisect.bisect_right(track[self.a[mid2]], right)

        if(t2 - t1 >= threshold):
            return self.a[mid2]

        return -1
