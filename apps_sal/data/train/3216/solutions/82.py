def movie(card, ticket, perc):
    numero_de_tickets = 0
    novo_valor_do_ticket = ticket * perc
    valor_inteiro_do_ticket = 0
    while valor_inteiro_do_ticket <= int(card) + 1:
        card += novo_valor_do_ticket
        valor_inteiro_do_ticket += ticket
        novo_valor_do_ticket *= perc
        numero_de_tickets += 1
    return numero_de_tickets
