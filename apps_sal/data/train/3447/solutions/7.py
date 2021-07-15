def next_perfect_square(n):
    if n<0:return 0
    is_square=lambda s:int(s**0.5)**2==s
    n+=1
    while not is_square(n):
        n+=1
    return n
