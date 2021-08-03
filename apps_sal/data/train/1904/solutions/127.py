class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []
        indices = {}

        for i in range(len(points)):
            curr_point = points[i]
            distance = math.sqrt(curr_point[0]**2 + curr_point[1]**2)
            heapq.heappush(heap, distance)
            if distance in list(indices.keys()):
                indices[distance].append(i)
            else:
                indices[distance] = [i]

        result = []
        i = 0
        while i < K:
            curr_distance = heapq.heappop(heap)
            curr_indices = indices[curr_distance]
            for index in curr_indices:
                result.append(points[index])
                i += 1

        return result
