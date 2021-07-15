def string_to_number(s):
    # ... your code here
    num = 0
    flag = False
    if s[0] == '-':
        flag = True
    for i in range(len(s)):
        if flag and i == 0: 
            continue
        else:
            num += int(s[i])
            if i != len(s) - 1:
                num *= 10
    return num if not flag else -1* num

