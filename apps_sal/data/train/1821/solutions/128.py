class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)
        
    # 4 1 6 6 8 2
    def mergeSort(self, arr, i, j):
        if i == j:
            return [arr[i]]
        
        mid = i + (j - i) // 2
        
        left_arr = self.mergeSort(arr, i, mid)
        right_arr = self.mergeSort(arr, mid + 1, j)
    
        return self.merge(left_arr, right_arr)
    
    def merge(self, a, b):
        res = []
        i = 0
        j = 0
        
        while len(res) < len(a) + len(b):
            if j == len(b) or (i < len(a) and a[i] < b[j]):
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
            
        return res
