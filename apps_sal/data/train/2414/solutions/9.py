class Solution:
    def countGoodTriplets(self,arr,a,b,c):
        ln,res = len(arr),0
        for i in range(ln-2):
            n = arr[i]
            for j in range(i+1,ln-1):
                n2 = arr[j]
                for k in range(j+1,ln):
                    n3 = arr[k]
                    if abs(n-n2)<=a and abs(n2-n3)<=b and abs(n-n3)<=c:
                        res+=1
        return res
