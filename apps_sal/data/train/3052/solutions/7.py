def remove(s):
    string = ''
    for i in range(len(s)):
        if s[i] != '!':
            string += s[i]
    count = 0
    for i in range(-1,-(len(s)-1),-1):
        if s[i] == '!':
            count += 1
        else:
            break
    return string + count*'!'
