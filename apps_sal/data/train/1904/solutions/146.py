\"\"\"
10, 14, 11, 15 12
10, 11, 14, 15
\"\"\"

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def swap(arr, idx1, idx2):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        
        def swapElement(idx1, idx2):
            swap(self.array, idx1, idx2)
            swap(self.distance, idx1, idx2)
            
        def Partition(low, high, index) -> int:
            \"\"\"
            Returns the new index
            \"\"\"
            partDistance = self.distance[index]
            swapElement(high, index)
            newIndex = low
            for i in range(low, high):
                if (self.distance[i] < partDistance):
                    swapElement(newIndex, i)
                    newIndex += 1
            
            swapElement(newIndex, high)
            return newIndex
        
        def Util(k):
            low = 0
            high = len(self.distance) - 1
            while (low <= high):
                index = random.randint(low, high)
                newIndex = Partition(low, high, index)
                if (newIndex == k):
                    return self.array[:k]
                if (newIndex > k):
                    high = newIndex - 1
                else:
                    low = newIndex + 1
        if (len(points) == K):
            return points
        self.array = points
        self.distance = []
        for point in points:
            self.distance.append(math.sqrt(point[0]**2 + point[1]**2))
        print(self.distance)
        return Util(K)
            
            
