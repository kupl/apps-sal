class Solution:
    def getdiff(self, x: int, y: int, m: int) -> int:
        return(abs(x-y) <= m)
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    x = arr[i]
                    y = arr[j]
                    z = arr[k]
                    # print(x,y,z)
                    if (self.getdiff(x,y,a) and self.getdiff(y,z,b) and self.getdiff(x,z,c)):
                        count += 1
        return(count)
