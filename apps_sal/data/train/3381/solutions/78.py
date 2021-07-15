def get_real_floor(n):
    if 0<=n<=1:
        return 0
    elif n>13:
        return n-2
    elif 1<n<=13:
        return n-1
    else:
        return n
