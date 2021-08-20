class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dictionary = {}
        for i in points:
            dictionary[i[0], i[1]] = math.sqrt((i[0] - 0) ** 2 + (i[1] - 0) ** 2)
        heap = []
        heapq.heapify(heap)
        for i in list(dictionary.keys()):
            heapq.heappush(heap, (dictionary[i], i))
        result = []
        for i in range(K):
            result.append(heapq.heappop(heap)[1])
        return result
