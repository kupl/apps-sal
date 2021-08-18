class Solution:
    import random

    def sortArray(self, nums: List[int]) -> List[int]:

        self.heapSort(nums)
        return nums

    def quickSort(self, arr):
        def partition(arr, l, h):
            if l >= h:
                return
            pivot = arr[random.randint(l, r)]
            tempL, tempH = l, h
            while tempL <= tempH:
                while tempL <= tempH and arr[tempL] < pivot:
                    tempL += 1
                while tempL <= tempH and arr[tempH] > pivot:
                    tempH -= 1
                if tempL <= tempH:
                    arr[tempL], arr[tempH] = arr[tempH], arr[tempL]
                    tempL += 1
                    tempH -= 1
            partition(arr, l, tempH)
            partition(arr, tempL, h)
            return
        partition(arr, 0, len(arr) - 1)
        return arr

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        self.mergeSort(L)
        self.mergeSort(R)
        idxL = 0
        idxR = 0
        idxA = 0
        while idxA < len(arr):
            if idxL < len(L) and idxR < len(R):
                if L[idxL] < R[idxR]:
                    arr[idxA] = L[idxL]
                    idxL += 1
                else:
                    arr[idxA] = R[idxR]
                    idxR += 1
            elif idxL < len(L):
                arr[idxA] = L[idxL]
                idxL += 1
            else:
                arr[idxA] = R[idxR]
                idxR += 1
            idxA += 1
        return arr

    def heapSort(self, arr):
        def heapify(arr, arrLen, i):
            l = 2 * i + 1
            r = l + 1
            largestIdx = i

            if l < arrLen and arr[largestIdx] < arr[l]:
                largestIdx = l
            if r < arrLen and arr[largestIdx] < arr[r]:
                largestIdx = r

            if largestIdx != i:
                arr[i], arr[largestIdx] = arr[largestIdx], arr[i]
                heapify(arr, arrLen, largestIdx)

        arrLen = len(arr)
        for i in range(arrLen // 2, -1, -1):
            heapify(arr, arrLen, i)

        for i in range(arrLen - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
