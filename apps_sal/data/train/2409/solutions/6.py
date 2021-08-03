class Solution:
    def maximum69Number(self, num: int) -> int:
        str_num = list(str(num))
        for i in range(len(str_num)):
            if int(str_num[i]) == 6:
                str_num[i] = '9'
                break
        print(str_num)
        str_num = ''.join(str_num)
        return int(str_num)
