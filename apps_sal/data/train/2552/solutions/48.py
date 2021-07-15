class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n/4.0
        print (threshold)
        oldnum = None
        for num in arr:
            # print (oldnum, num)
            if oldnum==num: 
                count += 1
                if count>threshold:
                    return num
            else:
                count=1
                oldnum=num
                
        if count>threshold:
            return num
