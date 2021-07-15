class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse = True)
        count = 0
        temp = 501
        
        for i in range(len(arr)):
            print(temp,',',count)
            if arr[i] != temp:
                if temp == count:
                    return temp
                temp = arr[i]
                count = 1
            else:
                count += 1
            print(temp,',,',count)
        if temp == count:
            return temp
        
        return -1
