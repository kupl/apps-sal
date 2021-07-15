def house_of_cards(n):
    if n < 1:
        raise error
    return 3*(n)*(n+1)//2 + 2*(n+1)
