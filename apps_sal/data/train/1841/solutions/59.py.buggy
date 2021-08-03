class Solution(object):
    def sign(self, num):
        if num==0:
            return 0
        elif num>0:
            return 1
        else:
            return -1
    def getStrongest(self, arr, k):
        \"\"\"
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        \"\"\"
        #from numpy import sign
        arr=sorted(arr)
        le=len(arr)
        if le==0:
            return []
        median=arr[int((le-1)/2)]
        strong=sorted([(abs(median-l),self.sign(l-median)) for l in arr])[-k:]
        #print(median, [abs(median-l)+Solution.sign([],l-median) for l in arr], strong)
        return [median+boo*i for i, boo in strong]
        
