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
                 
             else: # bits[i] is 0
                 i += 1
         # index: 0,1,2,..., L-2, L-1, where L denotes len(bits)
         if i == len(bits): # i comes from i+=2 case, bits[L-2] is 1, current i is one more of the last index, i.e. len(bits)
             return False   # ...10
         
         else:              # i comes from i+=1 case, bits[L-2] is 0, current i is the last index, len(bits)-1
             return True    # ...00
         """

        # Approach 2, much faster, scan from the back, till see a zero or exhaust the list
        # count how many one's there is.
        # Reason: ????...???0xxxx0  Only xxxx0 matters.  After a 0, start the process again.
        # 0 always marks the end of the earlier bits.
        count = 0
        i = len(bits) - 2  # s[len(s)-1] the last item in s is always 0.
        while i >= 0 and bits[i] is not 0:
            count += 1
            i -= 1

        if (count % 2) == 0:
            return True
        else:
            return False
