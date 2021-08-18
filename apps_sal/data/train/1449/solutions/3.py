tcase = int(eval(input()))
i = 0
while(tcase):
    tcase -= 1
    a = str(input())
    j = 0
    i = 0
    rem = 0
    length = len(a)
    ans = (length * (length + 1)) / 2
    while(i < length):
        if(a[i] == '7'):
            rem += (i - j + 1)
        else:
            j = i + 1
        i += 1
    ans -= rem
    print(ans)
