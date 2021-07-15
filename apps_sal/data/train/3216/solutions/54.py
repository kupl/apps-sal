import math

def movie(card, ticket, perc):
    number_of_tickets = 0
    scenario_a = 0
    scenario_b = 1
    
    while scenario_a <= scenario_b:
        number_of_tickets += 1
        scenario_a = number_of_tickets * ticket
        scenario_b = math.ceil(card + ticket * (1 - perc ** number_of_tickets) / (1 - perc))     
    return number_of_tickets-1
                

