class Solution:
    def maximum69Number(self, num: int) -> int:

        set_max = {9: 9, 99: 99, 999: 999, 9999: 9999, 6: 9, 66: 96, 666: 966, 6666: 9666}
        try:
            return set_max[num]
        except:
            num = str(num)
            for i in range(len(num)):
                if num[i] == '6':
                    return int(num[0:i] + '9' + num[i + 1:])
