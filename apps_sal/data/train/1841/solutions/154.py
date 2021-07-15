import heapq;
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort();
        median = (len(arr) - 1)//2;
        
        new_arr = [(abs(arr[median] - arr[0]),arr[0])];
        heapq.heapify(new_arr);
        
        for i in range(1, len(arr)):
            if len(new_arr) < k:
                heapq.heappush(new_arr, (abs(arr[median] - arr[i]),arr[i]));
            else:
                heapq.heappushpop(new_arr, (abs(arr[median] - arr[i]), arr[i]));
        
        final_arr = [];
        for i in range(len(new_arr)):
            final_arr.append(new_arr[i][1]);
        
        return final_arr;
