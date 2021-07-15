class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,1000001):
            flag=0
            sum=i;
            for j in nums:
                sum+=j
                if sum<1:
                    flag=1
                    break
            if flag==0:
                return i

