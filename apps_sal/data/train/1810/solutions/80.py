class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        counterMap = {}
        written = []
        
        for file in names:
            
            counter=counterMap.get(file, 0)
            
            # if in map, add number loop until found
            file_name=file
            if counter > 0:
                while file_name in counterMap:
                    file_name = file+\"(\"+str(counter)+\")\"
                    counter+=1
                    
                counterMap[file_name]=1
            else:
                counter += 1
            
            
            counterMap[file]=counter
            written.append(file_name)
           # print(counterMap)
        
        return written
