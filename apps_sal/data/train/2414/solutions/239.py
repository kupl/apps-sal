class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        out = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if(abs(arr[i] - arr[j]) <= a):
                    for k in range(j + 1, len(arr)):
                        if(abs(arr[j] - arr[k]) <= b):
                            if(abs(arr[i] - arr[k]) <= c):
                                out += 1

        return out

# # Brute Force Solution
# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

#         count = 0

#         for i in range(0,len(arr)-2):
#             for j in range(i+1,len(arr)-1):

#                 a_bool = abs(arr[i] - arr[j]) <= a

#                 # break case
#                 if a_bool:
#                     for k in range(j+1,len(arr)):

#                         b_bool = abs(arr[j] - arr[k]) <= b

#                         if b_bool:

#                             c_bool = abs(arr[i] - arr[k]) <= c

#                             if c_bool:
#                                 count += 1

#         return count
