import functools
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        lmax = lambda xs: functools.reduce(lambda x, y: x+y, xs)
        print(lmax(['1','2','3'])) 
        str_num = list(str(num))
        for i in range(len(str_num)):
            if int(str_num[i]) == 6:
                str_num[i] = '9'
                break
        #str_num = ''.join(str_num)
        str_num = lmax(str_num)
        return int(str_num)
