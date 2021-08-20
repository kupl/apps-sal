t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    arr = ['A', 'E', 'I', 'O', 'U']
    if n == 1:
        print('No')
    elif s[0] in arr and s[n - 1] in arr:
        print('Yes')
    else:
        for i in range(n - 1):
            if s[i] in arr and s[i + 1] in arr:
                flag = True
                break
            else:
                flag = False
        if flag == True:
            print('Yes')
        else:
            print('No')
