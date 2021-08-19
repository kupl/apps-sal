class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #         subArrayLengths = []
        #         for i in range(len(arr)):
        #             if (i+1)%2!=0:
        #                 subArrayLengths.append(i+1)
        #         print(subArrayLengths)

        #         subSum=0
        #         totalSum=0
        #         totalSum=0
        #         subSum=0
        #         flag=True
        #         subIndex=0
        #         while flag==True:

        #             if subIndex==len(arr) or subIndex==len(arr)-1:
        #                 flag = False
        #             else:
        #                 subIndex+=2
        #         return totalSum

        flag = True
        i = 1
        subSum = 0
        totalSum = 0
        while flag:
            subFlag = True
            start = 0
            end = i
            while subFlag:
                for j in arr[start:end]:
                    subSum += j
                if end == len(arr):
                    totalSum += subSum
                    print((subSum, totalSum))

                    subSum = 0
                    subFlag = False
                else:
                    start += 1
                    end += 1
            if i == len(arr) or i == len(arr) - 1:
                flag = False
            else:
                i += 2

        return totalSum
