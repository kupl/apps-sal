t = int(input())
while t:
    x = int(input())
    ans = ''
    if(x & 1):
        cc = ['2' if x == '1' else '1' for x in list(bin(x)[2:-1])]
        for x in cc:
            ans = ans + str(x)
        print(ans)
    else:
        print('0')
    t = t - 1
