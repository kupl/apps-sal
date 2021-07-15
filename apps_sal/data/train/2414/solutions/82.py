# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         #li = []
#         count = 0
#         for x in range(len(arr)):
#             #print(x)
#             for i in range(x+1,len(arr)):
#                 if (abs(arr[x]-arr[i]) <= a):
#                     for j in range(i+1,len(arr)):
#                         if (abs(arr[i]-arr[j])<=b):
#                             if (abs(arr[j]-arr[x])<=c):
#                                 count += 1
#         # for x in li:
#         #     if abs(x[0]-x[1]) <= a and abs(x[1]-x[2]) <=b and abs(x[0]-x[2]) <=c:
#         #         count += 1
#         return count

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        out=0
        
        for i in range(len(arr)):
                for j in range(i+1,len(arr)):        
                        for k in range(j+1,len(arr)):
                            if (abs(arr[i]-arr[j])<=a) and (abs(arr[j]-arr[k])<=b) and (abs(arr[i]-arr[k])<=c):
                                
                                    out+=1
        return out
