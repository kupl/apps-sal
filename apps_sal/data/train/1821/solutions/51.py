class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Heap Sort, building max heap
        l=len(nums)
        def heapify(i: int, l: int) -> None:
            if 2*i+2==l:
                if nums[i]<nums[2*i+1]:
                    nums[i], nums[2*i+1]=nums[2*i+1], nums[i]
            elif 2*i+2<l:
                if nums[2*i+1] > nums[2*i+2]:
                    if nums[i]<nums[2*i+1]:
                        nums[i], nums[2*i+1]=nums[2*i+1], nums[i]
                    heapify(2*i+1, l)
                else:
                    if nums[i]<nums[2*i+2]:
                        nums[i], nums[2*i+2]=nums[2*i+2], nums[i]
                    heapify(2*i+2, l)
                        
        #building the heap
        for i in range((l-1)//2, -1, -1):
            heapify(i, l)
        
        #swap the top with the last item and decrease the heap by 1, rebuilding the heap
        for i in range(l-1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)
            
        return nums
        
        \"\"\"
        #Quick sort
        def quickSort(start:int, end:int) -> None:
            if start>=end:
                return
            if (end==start+1):
                if nums[end]<nums[start]:
                    nums[end], nums[start] = nums[start], nums[end]
                return
            pivit=nums[end]
            left, right=start, end-1
            while left<=right:
                while left<=end-1 and nums[left]<=pivit:
                    left+=1
                while right>=start and nums[right]>=pivit:
                    right-=1
                if left<right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left+=1
                    right-=1
            nums[left], nums[end] = nums[end], nums[left]
            quickSort(start, left-1)
            quickSort(left+1, end)
            
        quickSort(0, len(nums)-1)
        return nums
        \"\"\"
        
        \"\"\"
        #Merge Sort
        def merge(l1:List[int], l2:List[int]) -> List[int]:
            ret =[]
            i1=i2=0
            while i1<len(l1) and i2<len(l2):
                if l1[i1]<l2[i2]:
                    ret.append(l1[i1])
                    i1+=1
                else:
                    ret.append(l2[i2])
                    i2+=1
            if i1==len(l1):
                ret+=l2[i2:]
            else:
                ret+=l1[i1:]
            return ret
        
        def mergeSort(start:int, end:int) -> List[int]:
            if start>=end:
                return [nums[start]]
            if start+1==end:
                if nums[start]>nums[end]:
                    nums[start], nums[end]=nums[end], nums[start]
                return [nums[start], nums[end]]
            mid=(start+end)//2
            return merge(mergeSort(start, mid), mergeSort(mid+1, end))
            
        return mergeSort(0, len(nums)-1)
        \"\"\"
        
        
