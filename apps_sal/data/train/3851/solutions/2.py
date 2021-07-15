def interest(money, rate, periods):
    simple = money * (1 + rate * periods)
    compound = money * (1 + rate) ** periods
    return [round(simple), round(compound)]
