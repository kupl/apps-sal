class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        else:
            numA = self.sortArray(nums[:len(nums)//2])
            numB = self.sortArray(nums[len(nums)//2:])
            i,j = 0,0
            nums = []
            while i<len(numA) and j<len(numB):
                if numA[i]<=numB[j]:
                    nums.append(numA[i])
                    i+=1
                else:
                    nums.append(numB[j])
                    j+=1
            if i==len(numA):
                nums+=numB[j:]
            else:
                nums+=numA[i:]
        return nums

