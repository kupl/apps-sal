def counting_valleys(s): 
    s = list(s)
    s = list(filter(lambda x: x != 'F', s))
    for i in range(len(s)):
        if s[i] == 'D':
            s[i] = -1
        if s[i] == 'U':
            s[i] = 1
    count = 0
    sum = 0
    for i in range(len(s)):
        sum += s[i]
        if sum == 0 and s[i] == 1:
            count += 1
    return count
