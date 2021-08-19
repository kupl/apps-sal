class Solution:

    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        '\n         i = 0\n         while i < len(bits)-1:\n             if bits[i] == 1:\n                 i += 2\n                 \n             else: # bits[i] is 0\n                 i += 1\n         # index: 0,1,2,..., L-2, L-1, where L denotes len(bits)\n         if i == len(bits): # i comes from i+=2 case, bits[L-2] is 1, current i is one more of the last index, i.e. len(bits)\n             return False   # ...10\n         \n         else:              # i comes from i+=1 case, bits[L-2] is 0, current i is the last index, len(bits)-1\n             return True    # ...00\n         '
        count = 0
        i = len(bits) - 2
        while i >= 0 and bits[i] is not 0:
            count += 1
            i -= 1
        if count % 2 == 0:
            return True
        else:
            return False
