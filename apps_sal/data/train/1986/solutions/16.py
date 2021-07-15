class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        currentList = [\"0\", \"1\"]
        
        from copy import deepcopy
        
        for idx in range(n-1):
            length_prev = len(currentList)
            for idx in range(length_prev-1, -1, -1):
                currentList.append(\"1\"+currentList[idx])
            
            for idx in range(length_prev):
                currentList[idx] = \"0\"+currentList[idx]
                
        for idx in range(len(currentList)):
            currentList[idx] = int(currentList[idx], 2)
         
        idx = currentList.index(start)
        currentList = currentList[idx:] + currentList[:idx]
        return currentList
            
            
