class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        L=len(arr)
        if L<3:
            return 0
        count=0
        def check(i,j,k):
            if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                return True
            return False
        for i in range(L-2):
            for j in range(i+1,L-1):
                for k in range(j+1,L):
                    if check(i,j,k):
                        count+=1
        return count
