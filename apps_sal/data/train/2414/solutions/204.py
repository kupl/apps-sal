class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        total = 0 
        if n < 3:
            return None
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    A= abs(arr[i]-arr[j])  
                    B= abs(arr[j] -arr[k])
                    C= abs(arr[i]- arr[k])
                    if A<=a and B<=b and C<=c:
                        total +=1
        
        return total

    


