for _ in range(int(input())):
    s = input()
    for i in range(0, len(s), 2):
        if s[i] == 'A' and s[i + 1] == 'B' or (s[i] == 'B' and s[i + 1] == 'A'):
            c = 1
        else:
            print('no')
            c = 0
            break
    if c == 1:
        print('yes')
