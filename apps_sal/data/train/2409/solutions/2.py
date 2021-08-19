class Solution:
    def maximum69Number(self, num: int) -> int:
        ###############################################################
        # Solution 1,
        # num_str = list(str(num))  # convert to string list
        # if num_str == ['9']*len(num_str): # check if it needs change
        #     return num
        # else:
        #     for i in range(len(num_str)):
        #         if num_str[i] == '6': # chenge the '6' to '9'
        #             num_str[i] = '9'
        #             return int(''.join(num_str))

        ###############################################################
        # Solution 2, using just string
        set_max = {9: 9, 99: 99, 999: 999, 9999: 9999, 6: 9, 66: 96, 666: 966, 6666: 9666}
        try:
            return set_max[num]
        except:
            num = str(num)
            for i in range(len(num)):
                if num[i] == '6':
                    return int(num[0:i] + '9' + num[i + 1:])
        ###############################################################
