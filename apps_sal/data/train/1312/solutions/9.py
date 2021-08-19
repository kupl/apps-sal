t = int(input())
while t:
    t -= 1
    (r, c) = list(map(int, input().split(' ')))
    l = [''] * c
    flag = 0
    while r:
        r -= 1
        str = input()
        if 'spoon' in str.lower():
            flag = 1
        else:
            j = 0
            for char in list(str):
                l[j] += char
                j += 1
    for str1 in l:
        if 'spoon' in str1.lower():
            flag = 1
            break
    if flag == 1:
        print('There is a spoon!')
    if flag == 0:
        print('There is indeed no spoon!')
