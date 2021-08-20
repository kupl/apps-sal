for i in range(int(input())):
    s = input()
    count = 0
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            count += 1
    if s[0] != s[-1]:
        count += 1
    if count <= 2:
        print('uniform')
    else:
        print('non-uniform')
