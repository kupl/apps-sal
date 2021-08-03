def numberAndIPaddress(s):
    if '.' in s:
        ans = str(int(''.join("{:0>8b}".format(int(n)) for n in s.split('.')), 2))
    else:
        s32 = "{:0>32b}".format(int(s))
        ans = '.'.join(str(int(s32[8 * i:8 * (i + 1)], 2)) for i in range(4))
    return ans
