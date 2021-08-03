# cook your dish here
try:
    t = int(input())
    for k in range(t):
        s = input()
        ans = 0
        if((len(s) % 2 != 0) or (not '0' in s) or (not '1' in s)):
            ans = -1
        else:
            zeros = 0
            ones = 0
            for i in s:
                if i == '1':
                    ones += 1
                else:
                    zeros += 1
            ans = abs(zeros - ones) // 2
        print(ans)
except:
    pass
