class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.TimeMaps=collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.TimeMaps[key].append((timestamp,value))
        

#     # binary search with repeated values    
#     def get(self, key: str, timestamp: int) -> str:
        
#         # get all the values with the same key
#         arr=self.TimeMaps[key]

#         if not arr: return ''
        
#         # sort by timestamp
#         arr.sort(key=lambda x: x[0])
 
#         l=0
#         r=len(arr)-1
#         res=-1
#         while l<=r:
            
#             m=l+(r-l)//2
            
#             if arr[m][0]==timestamp:
#                 return arr[m][1]
            
#             if arr[m][0]>timestamp:
#                 r=m-1
#             else:
#                 res=m
#                 l=m+1

#         return arr[res][1] if res !=-1 else ''


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMaps:
            return ''
        return self.b_search(self.TimeMaps[key], timestamp)

    def b_search(self, lst, target):
        left, right = 0, len(lst) - 1
        res = ''
        while left <= right:
            mid = left + (right - left) // 2
            item = lst[mid]
            if item[0] == target:
                return item[1]
            if item[0] > target:
                right = mid - 1
            else:
                left = mid + 1
                res = item[1]
        return res
        

