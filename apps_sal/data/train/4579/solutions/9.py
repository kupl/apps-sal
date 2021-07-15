def pattern(n):
    d = int(str(n)[-1])
    ptn = str(d) * n
    arr = [ptn]
    for i in range(n-1):
        if ptn[-1] != '0':
            ptn = ptn[:i+1] + str(int(ptn[-1])-1) * (n-i-1)
        else:
            ptn = ptn[:i+1] + '9' * (n-i-1)
        arr.append(''.join(ptn))
    result = ('\n').join(arr)
    return result

