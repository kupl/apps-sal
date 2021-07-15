def split_the_bill(x):
    bill = float(sum(amount for amount in x.values())) / len(x)
    return {person : round(amount - bill, 2) for person, amount in x.items()}
