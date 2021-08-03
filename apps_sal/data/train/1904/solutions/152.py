class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist_square(i): return points[i][0] ** 2 + points[i][1] ** 2

        def sort(i: int, j: int, K: int):
            # partially sorts points[i...j+1] so the first K elements are the
            # smallest K elements
            if i >= j:
                return

            # put random element as points[i] as the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]  # ???

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i: int, j: int) -> int:
            # partition by pivot points[i], returning an index mid such that
            # points[i] <= points[mid] <= points[j] for i < mid < j
            oi = i
            pivot = dist_square(i)
            i += 1

            while True:
                while i < j and dist_square(i) < pivot:
                    i += 1
                while i <= j and dist_square(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
