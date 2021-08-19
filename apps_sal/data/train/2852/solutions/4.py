def find_longest(st):
    n = len(st)
    lis = []
    lis.append(-1)
    result = 0
    for i in range(n):
        if st[i] == '(':
            lis.append(i)
        else:    # If closing bracket, i.e., str[i] = ')'
            lis.pop()
            if len(lis) != 0:
                result = max(result, i - lis[len(lis) - 1])
            else:
                lis.append(i)
    return result
