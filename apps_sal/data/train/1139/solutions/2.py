def numDecodings(s):
    s = '10' + s
    dec = [1] * (len(s) + 2)
    for i in range(2, len(s)):
        if s[i] == '0':
            if s[i - 1] != '1' and s[i - 1] != '2':
                return 0
            dec[i] = dec[i - 2]
        elif int(s[i - 1:i + 1]) > 26 or int(s[i - 1:i + 1]) < 10:
            dec[i] = dec[i - 1]
        else:
            dec[i] = dec[i - 1] + dec[i - 2]
    return dec[len(s) - 1]


for _ in range(int(input())):
    nums = input()
    ways = numDecodings(nums)
    print(['NO', 'YES'][ways % 2 == 0])
