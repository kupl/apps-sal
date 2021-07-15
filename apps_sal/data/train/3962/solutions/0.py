def house_of_cards(n):
    if n>=1:
        return(n+1)*n/2 + (n+2)*(n+1)
    raise ValueError
