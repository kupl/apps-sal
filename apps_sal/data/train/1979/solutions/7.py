class Solution:
    def check_valid_hour(self, arr:List[int], i: int, j: int) -> bool:
        minutes_index = [x for x in [0,1,2,3] if x != i and x != j]
        minutes = max(int(str(arr[minutes_index[0]])+str(arr[minutes_index[1]])), int(str(arr[minutes_index[1]])+str(arr[minutes_index[0]]))) 
        
        if minutes >= 60:
            minutes = min(int(str(arr[minutes_index[0]])+str(arr[minutes_index[1]])), int(str(arr[minutes_index[1]])+str(arr[minutes_index[0]])))             
        
        if minutes >= 60:
            return False
        return True
    
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if len(arr) == 0:
            return \"\"
        
        index_i = -1
        index_j = -1
        max_hour = -1
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if int(str(arr[i])+str(arr[j])) < 24 and int(str(arr[i])+str(arr[j])) >= max_hour and self.check_valid_hour(arr,i,j):
                        max_hour = int(str(arr[i])+str(arr[j]))
                        index_i = i
                        index_j = j
        
        minutes_index = [x for x in [0,1,2,3] if x != index_i and x != index_j]
        
        if max_hour == -1:
            return \"\"
        elif max_hour == 0:
            max_hour = \"00\"
        if index_i == -1 and index_j == -1:
            minutes = \"00\"
        else:
            minutes = max(int(str(arr[minutes_index[0]])+str(arr[minutes_index[1]])), int(str(arr[minutes_index[1]])+str(arr[minutes_index[0]]))) 
        
        if minutes >= 60:
            minutes = min(int(str(arr[minutes_index[0]])+str(arr[minutes_index[1]])), int(str(arr[minutes_index[1]])+str(arr[minutes_index[0]])))             
        
        if minutes >= 60:
            return \"\"
        str_minutes = str(minutes)
        str_hours = str(max_hour)
        if len(str_minutes) == 1:
            str_minutes = \"0\" + str_minutes
        if len(str_hours) == 1:
            str_hours = \"0\" + str_hours
    
        return str_hours+\":\"+str_minutes
        
                
                
            
        
            
        
