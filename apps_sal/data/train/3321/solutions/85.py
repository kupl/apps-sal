def evil(n):
    r = 0
    while n > 0:
        r += n%2
        n //= 2
    
    return "It's Odious!" if r%2 else "It's Evil!"
