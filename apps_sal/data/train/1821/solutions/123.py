class Solution:
    def merge(self, left, mid, right, arr):

        i = left
        j = mid + 1

        temp = []
        while(i <= mid and j <= right):

            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while(i <= mid):
            temp.append(arr[i])
            i += 1

        while(j <= right):
            temp.append(arr[j])
            j += 1

        j = 0
        for i in range(left, right + 1):
            arr[i] = temp[j]
            j += 1

    def mergesort(self, left, right, arr):
        if left >= right:
            return
        else:
            mid = (left + right) // 2

            self.mergesort(left, mid, arr)

            self.mergesort(mid + 1, right, arr)

            self.merge(left, mid, right, arr)

            return

    def insertionSort(self, arr):
        n = len(arr)

        for i in range(1, n):

            key = arr[i]

            j = i - 1

            while(j >= 0 and key < arr[j]):

                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

    def heapify(self, index, n, arr):
        i = index
        left = 2 * i + 1
        right = 2 * i + 2
        max_index = i
        while(left < n):

            if arr[left] > arr[max_index]:
                max_index = left

            if right < n:

                if arr[right] > arr[max_index]:
                    max_index = right

            if max_index == index:
                break

            arr[max_index], arr[index] = arr[index], arr[max_index]

            index = max_index
            left = 2 * index + 1
            right = 2 * index + 2

    def heapsort(self, arr):

        n = len(arr)

        for i in range(0, n):

            self.heapify(n - i - 1, n, arr)

        for i in range(0, n):

            arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]

            self.heapify(0, n - i - 1, arr)

    def sortArray(self, nums: List[int]) -> List[int]:

        self.heapsort(nums)
        return nums
