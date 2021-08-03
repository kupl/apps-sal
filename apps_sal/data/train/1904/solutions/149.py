class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        left = 0
        right = len(points) - 1
        target = K - 1
        while (left <= right):
            rand_pivot = random.randint(left, right)
            pivot = self.partition(left, right, rand_pivot, points)
            if (pivot == target):
                return points[0: pivot + 1]
            elif (pivot < target):
                left = pivot + 1
            else:
                right = pivot - 1

    def partition(self, i, j, pivot, arr):
        pivot_element = self.distFromOrigin(arr[pivot])
        self.swap(pivot, j, arr)
        result = i
        for x in range(i, j):
            if self.distFromOrigin(arr[x]) < pivot_element:
                self.swap(x, result, arr)
                result += 1
        self.swap(result, j, arr)
        return result

    def swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def distFromOrigin(self, point):
        return math.sqrt((point[0] ** 2 + point[1] ** 2))
