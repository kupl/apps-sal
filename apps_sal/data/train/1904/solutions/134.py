'''

- preprocess, store (distance, (x,y))
- init heap w/ k
- push pop for the rest
- return heap

- O(k) + O(N-K log K) / O(n)
- O(K log N) / O(n)

'''
# O(nlogk) / O(k)


class Point:
    def __init__(self, pt):
        self.distance = -1 * sqrt(pt[0]**2 + pt[1]**2)
        self.pt = pt

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap)

        for pt in points:
            curr_pt = Point(pt)

            if len(heap) < K:
                heapq.heappush(heap, curr_pt)
            else:
                heapq.heappushpop(heap, curr_pt)

        return [pt.pt for pt in heap]
