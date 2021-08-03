
T = int(input())

for q in range(T):
    n = int(input())
    s = input()
    flag = 0
    for i in range(n - 1):
        if (s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
            if (s[i + 1] == 'A' or s[i + 1] == 'E' or s[i + 1] == 'I' or s[i + 1] == 'O' or s[i + 1] == 'U'):
                flag = 1
                break

    if (s[n - 1] == 'A' or s[n - 1] == 'E' or s[n - 1] == 'I' or s[n - 1] == 'O' or s[n - 1] == 'U'):
        if (s[0] == 'A' or s[0] == 'E' or s[0] == 'I' or s[0] == 'O' or s[0] == 'U'):
            flag = 1

    if flag == 1 and n != 1:
        print('Yes')
    else:
        print('No')
