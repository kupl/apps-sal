
t = int(input())
while(t != 0):
    word = input()
    split_word = list(word)
    flag = 0
    x = 0
    y = -1
    while(x < len(split_word)):
        if split_word[x] != '.' and split_word[y] != '.':
            if split_word[x] != split_word[y]:
                flag = 1
                break
        elif(split_word[x] == split_word[y] and split_word[x] == '.' and split_word[y] == '.'):
            split_word[x] = 'a'
            split_word[y] = 'a'
        elif(split_word[x] == '.'):
            split_word[x] = split_word[y]
        elif(split_word[y] == '.'):
            split_word[y] = split_word[x]
        x += 1
        y -= 1

    if(flag == 1):
        print(-1)
    else:
        print(''.join(split_word))
    t = t - 1
