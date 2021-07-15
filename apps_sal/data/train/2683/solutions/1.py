def split_the_bill(spendings):
    fair_amount = sum(spendings.values()) / float(len(spendings))
    return {name: round(amount - fair_amount, 2) for name, amount in spendings.items()}

