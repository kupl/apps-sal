class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.countingSort(nums)
        return nums
        
                  
    def quickSort(self, arr):
        import random
        def partition(arr, l, h):
                if l>=h:
                    return
                #pivot = arr[random.randint(l,h)]
                pivot = arr[h]
                tempL, tempH = l, h
                while tempL<=tempH:
                    while tempL<=tempH and arr[tempL]<pivot:
                        tempL+=1
                    while tempL<=tempH and arr[tempH]>pivot:
                        tempH-=1
                    if tempL<=tempH:
                        arr[tempL], arr[tempH] = arr[tempH], arr[tempL]
                        tempL+=1
                        tempH-=1
                partition(arr, l, tempH)
                partition(arr, tempL, h)
                return
        partition(arr, 0, len(arr)-1)
        return arr
    
    def mergeSort(self, arr):
        if len(arr)<=1: return
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        self.mergeSort(L)
        self.mergeSort(R)
        idxL = 0
        idxR = 0
        idxA = 0
        while idxA<len(arr):
            if idxL < len(L) and idxR < len(R):
                if L[idxL]<R[idxR]:
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
            idxA+=1
        return arr
    
    def heapSort(self, arr):
        def heapify(arr, arrLen, i):
            # i = index of this node
            l = 2 * i + 1
            r = l + 1
            largestIdx = i
            
            # theese two if is to finding the biggest node to make a max heap 
            if l < arrLen and arr[largestIdx] < arr[l]:
                largestIdx = l
            if r < arrLen and arr[largestIdx] < arr[r]:
                largestIdx = r
            
            # make the largest the parent
            if largestIdx!=i:
                arr[i], arr[largestIdx] = arr[largestIdx], arr[i]
                heapify(arr, arrLen, largestIdx)
        
        arrLen = len(arr)
        # heap all the tree from the middle of the array to the front
        # make the end of the array biggest
        for i in range(arrLen//2, -1, -1):
            heapify(arr, arrLen, i)
        
        # the i is the root of the tree since i, and its a max heap
        for i in range(arrLen-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify (arr, i, 0)
            
    def countingSort(self, arr):
        maxA = arr[0]
        minA = arr[0]
        
        for a in arr:                           # O(len(arr))
            maxA = max(maxA, a)
            minA = min(minA, a)
            
        countLen = maxA-minA+1
        offset = - minA
        
        count = [0 for i in range(countLen)]    # O(max(arr)-min(arr))
        
        for a in arr:                           # O(len(arr))
            count[a + offset] += 1
        
        for i in range(1,countLen):             # O(max(arr))
            count[i] += count[i-1]
        
        res = list(arr)                  
        
        for r in res:
            arr[count[r + offset]-1] = r
            count[r + offset] -= 1
            
        return
