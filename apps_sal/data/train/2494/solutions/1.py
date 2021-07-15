class Solution:
    def defangIPaddr(self, address: str) -> str:
        stringArr  = address.split('.')
        
        return '[.]'.join(stringArr)
        
        
        
        

