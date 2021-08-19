for i in range(int(input())):
    s = list(input())
    for i in range(0, len(s), 2):
        if s[i] == s[i + 1]:
            print('no')
            break
        elif i == len(s) - 2:
            print('yes')
            break
        else:
            continue
