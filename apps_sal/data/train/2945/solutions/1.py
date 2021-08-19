def fortune(money, interest, withdraw, years, inflation):
    interest = 1 + interest / 100
    inflation = 1 + inflation / 100
    for _ in range(years - 1):
        money = int(money * interest - withdraw)
        if money < 0:
            return False
        withdraw *= inflation
    return True
