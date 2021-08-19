for _ in range(int(input())):
    n = int(input())
    s = input()
    if n == 1:
        print('No')
    else:
        count = 0
        if (s[0] == 'A' or s[0] == 'E' or s[0] == 'I' or (s[0] == 'O') or (s[0] == 'U')) and (s[n - 1] == 'A' or s[n - 1] == 'E' or s[n - 1] == 'I' or (s[n - 1] == 'O') or (s[n - 1] == 'U')):
            count = 1
        else:
            for i in range(n - 1):
                if (s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or (s[i] == 'O') or (s[i] == 'U')) and (s[i + 1] == 'A' or s[i + 1] == 'E' or s[i + 1] == 'I' or (s[i + 1] == 'O') or (s[i + 1] == 'U')):
                    count = 1
                    break
        if count == 1:
            print('Yes')
        else:
            print('No')
