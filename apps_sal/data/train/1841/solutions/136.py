class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        temp = sorted(arr)
        median = 0
        n = len(arr)
        median = temp[(n-1)//2]
        j = len(arr)-1
        i = 0
        res = []
        print(\"hi\",str(median))
        while i<=j:
            left = median - temp[i]
            right = temp[j] - median
            if left > right:
                res.append(temp[i])
                i+=1
            elif left < right:
                res.append(temp[j])
                j-=1
            else:
                if temp[i]>temp[j]:
                    res.append(temp[i])
                    i+=1
                else:
                    res.append(temp[j])
                    j-=1
            if len(res) == k:
                return res
        return res
