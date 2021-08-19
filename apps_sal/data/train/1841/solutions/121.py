class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        self.median = arr[(len(arr) - 1) // 2]
        count = 1
        (i, j) = (0, len(arr) - 1)
        values = []
        while count <= k:
            if self.key_func(arr[i]) > self.key_func(arr[j]):
                values.append(arr[i])
                i += 1
            elif self.key_func(arr[i]) < self.key_func(arr[j]):
                values.append(arr[j])
                j -= 1
            elif arr[i] > arr[j]:
                values.append(arr[i])
                i += 1
            else:
                values.append(arr[j])
                j -= 1
            count += 1
        return values

    def key_func(self, elem):
        return abs(elem - self.median)
