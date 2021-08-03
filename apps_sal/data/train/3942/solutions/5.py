def solve(n):
    bills = [500, 200, 100, 50, 20, 10]
    bills_amount = 0
    if n % 10 != 0:
        return -1
    else:
        for i in bills:
            bills_amount += int(n / i)
            n %= i
        return bills_amount
