def count_cows(n):
    if isinstance(n,int):
        if n<3: return 1
        return count_cows(n-1)+count_cows(n-3)
