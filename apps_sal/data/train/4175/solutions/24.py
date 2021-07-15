def repeater(s, n):
    dp = s
    for i in range(n-1): s+=dp
    return s
