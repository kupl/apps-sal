class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h_table = set()
        for num in arr:
            if num*2 in h_table or num/2 in h_table:
                return True
            h_table.add(num)
        return False
            
            
        

