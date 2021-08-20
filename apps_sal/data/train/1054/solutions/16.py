for _ in range(int(input())):
    str = list(input())
    l = len(str)
    flag = False
    for i in range(l // 2):
        if str[i] == '.':
            if str[-i - 1] == '.':
                str[i] = str[-i - 1] = 'a'
            else:
                str[i] = str[-i - 1]
        elif str[-i - 1] == '.':
            str[-i - 1] = str[i]
        elif str[i] != str[-i - 1]:
            print('-1')
            flag = True
            break
    if flag:
        continue
    if l % 2 != 0 and str[l // 2] == '.':
        str[l // 2] = 'a'
    print(''.join(str))
