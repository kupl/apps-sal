class TimeMap:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.__hash_map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.__hash_map:
            self.__hash_map[key].append((timestamp,value))
        else:
            self.__hash_map[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.__hash_map:
            arr=self.__hash_map[key]
            # arr.sort(key=lambda x:x[0])
            list_size=len(arr)
            l=0
            r=list_size-1
            while l<=r:
                mid=l+(r-l)//2
                if arr[mid][0]==timestamp:
                    return arr[mid][1]
                elif arr[mid][0]<timestamp:
                    l=mid+1
                else:
                    r=mid-1
                    #[8]   t=2
            if r< 0:
                return \"\"
            else:
                return arr[r][1]
        else:
            return \"\"

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
\"\"\"
[k,1][k,5][k,8][,1][,1]

\"\"\"
