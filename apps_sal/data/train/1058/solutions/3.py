for _ in range(int(input())):
    s = list(str(input()))
    for i in range(len(s)):
        s[i] = int(s[i]) - 2
    print(''.join([str(i) for i in s]))
