class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        """
         i = 0
         while i < len(bits)-1:
             if bits[i] == 1:
                 i += 2
                 
             else: 
                 i += 1
         if i == len(bits): 
             return False   
         
         else:              
             return True    
         """

        count = 0
        i = len(bits) - 2
        while i >= 0 and bits[i] is not 0:
            count += 1
            i -= 1

        if (count % 2) == 0:
            return True
        else:
            return False
