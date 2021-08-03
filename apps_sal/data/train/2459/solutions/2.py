class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        '''
         s = []
         hexChar= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
         if num == 0:
             return '0'
         while num:
             s.append(hexChar[num % 16])
             num = num // 16
         return "".join(s[::-1])
         hex(int())
         hex(num & 0b)
         '''
        return '%x' % (num & 0xffffffff)
