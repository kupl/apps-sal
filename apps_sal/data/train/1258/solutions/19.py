'''

This File is created by Saurabh Sisodia
email address... "ssisodia507@gmail.com"

................................................................................    ............

'''
for _ in range(int(input())):
    n = input()
    sum = 0
    len = 0
    for v in n:
        len += 1
        sum += int(v)
    rem = sum % 9
    if len > 1 and sum < 9:
        ans = 9 - rem
    else:
        ans = min(rem, 9 - rem)
    print(ans)
