n = int(input()) + 1
flag = 0
while(n <= 987654321):
    digits = [str(x) for x in str(n)]
    if '0' in digits:
        n += 1
        continue
    else:
        n += 1
        j = len(digits)
        s = len(list(set(digits)))
        if j == s:
            print(''.join(digits))
            flag = 1
            break
if flag == 0:
    print('0')
