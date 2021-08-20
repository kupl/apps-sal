class Solution:

    def find_smallest_and_second_smallest(self, a):
        smallest = a[0]
        c = 1
        for i in a:
            if i < smallest:
                smallest = i
                c = 1
            if i == smallest:
                c += 1
        smallest2 = True
        if c == 2:
            smallest2 = 999999
            for i in a:
                if i != smallest:
                    smallest2 = min(smallest2, i)
        return (smallest, smallest2)

    def givedp(self, arr):
        if len(arr) == 1:
            return min(arr[0])
        (a, b) = ('', '')
        for i in range(len(arr) - 1, -1, -1):
            if i != len(arr) - 1:
                for j in range(len(arr[i])):
                    if a == arr[i + 1][j] and b != True:
                        arr[i][j] += b
                    else:
                        arr[i][j] += a
            if i != 0:
                (a, b) = self.find_smallest_and_second_smallest(arr[i])
        return min(arr[0])

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        return self.givedp(arr)
