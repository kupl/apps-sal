class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = arr[0][:]

        for i, costs in enumerate(arr[1:], 1):
            prev = dp[:]
            
            for j, cost in enumerate(costs):
                dp[j] = cost + min(prev[:j] + prev[j+1:])

        return min(dp)
    
    
    
#         min_path_sum = float('inf')
        
#         def get_all_min_paths(arr, cur_row, cur_index, cur_sum):
#             nonlocal min_path_sum
#             if cur_row == len(arr):
#                 # print()
#                 min_path_sum = min(min_path_sum, cur_sum)
#             else: 
#                 current_row = arr[cur_row]
#                 for i in range(len(current_row)):
#                     if i != cur_index:
#                         ele = current_row[i]
#                         # print('cur_value', cur_index, 'ele', ele, 'cur_sum', cur_sum)
#                         get_all_min_paths(arr, cur_row+1, i, cur_sum+ele)
            
#             # pick one of the elements from the next row
#             # if its valye > cur 
#             # once reached len(arr) add path to array if its sum is 
#             # less than the current minimum 
            
        
        
#         get_all_min_paths(arr, 0, None, 0)
#         return min_path_sum 

