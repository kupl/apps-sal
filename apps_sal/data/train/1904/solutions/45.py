class Node:
    def __init__(self, c, sum):
        self.sum = sum
        self.c = c

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        heap = []
        ans = []
        for i in points:
            heap.append(Node(i, i[0]**2 + i[1]**2))
        n = len(heap)
        def heapify(arr, i, n):
            smallest = i
            left = i*2 + 1
            right = i*2 + 2
            if left < n and arr[i].sum > arr[left].sum:
                smallest = left
            if right < n and arr[right].sum < arr[smallest].sum:
                smallest = right
            if smallest != i:
                arr[smallest], arr[i] = arr[i], arr[smallest]
                heapify(arr, smallest, n)
        for i in range((n-1)//2,-1,-1):
            heapify(heap, i, n)
        while K > 0 and len(ans) < len(points):
            h = heap[0]
            ans.append(h.c)
            heap[0].sum = sys.maxsize
            heapify(heap, 0, len(heap))
            K -= 1
        return ans
