class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         triplets = []
#         arr_len = len(arr) - 1
        
#         for i in range(arr_len):
#             for j in range(i+1, arr_len):
#                 for k in range(j+1, arr_len):
#                     if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:  
#                         triplets.append((arr[i], arr[j], arr[k]))
#                         # triplets += 1
        
#         return len(triplets)

        C = list(combinations(arr,3))
        C = [self.checkGood(x,a,b,c) for x in C]
        C = [x for x in C if x != None]
        # print(C)
        return len(C)
    
    def checkGood(self,tup,a,b,c):
        if abs(tup[0] - tup[1]) <= a and abs(tup[0] - tup[2]) <= c and abs(tup[2] - tup[1]) <= b:
            return tup

