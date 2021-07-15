import math
def movie(card, ticket, perc):
    n=card//ticket
    system_go=True
    while system_go:
        system_A=ticket*n
        system_B=card+sum([ticket*perc**x for x in range(1,n+1)])
        if system_A<card:
            n+=1
            continue
        if system_A>math.ceil(system_B):
            return n
            break
        else:
            n+=1
