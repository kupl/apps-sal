def interest(principal, interest, periods):
    return [round(principal * (1 + interest * periods)),
            round(principal * (1 + interest) ** periods)]
