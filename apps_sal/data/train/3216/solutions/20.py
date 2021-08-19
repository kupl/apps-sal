def movie(card, ticketA, perc):
    assert perc < 1
    ticketB = ticketA
    priceA = times = 0
    priceB = card
    while not priceA > -(-priceB // 1):
        ticketB *= perc
        priceA += ticketA
        priceB += ticketB
        times += 1
    return times
