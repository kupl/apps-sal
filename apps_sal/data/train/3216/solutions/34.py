import math

def movie(card, ticket, perc):
    curr_card_price = card
    curr_ticket_price = 0
    next_card_purchase = ticket * perc
    trips = 0
    
    while math.ceil(curr_card_price) >= curr_ticket_price:
        curr_card_price += next_card_purchase
        curr_ticket_price += ticket
        
        trips += 1
        next_card_purchase *= perc

    return trips
