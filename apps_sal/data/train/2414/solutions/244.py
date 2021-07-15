class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):   
            for j in range(i+1,n):
                val1 = abs(arr[i]-arr[j])
                if val1<=a:
                    for k in range(j+1,n):
                        val2 = abs(arr[j]-arr[k])
                        if val2<=b:
                            val3 = abs(arr[i]-arr[k])
                            if val3<=c:
                                count += 1
        return count
                    

