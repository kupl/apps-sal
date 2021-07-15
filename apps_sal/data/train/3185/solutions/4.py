rotate_against_clockwise=lambda a,n:rotate_against_clockwise(list(zip(*a))[::-1],n-1) if n%4 else list(map(list,a))
