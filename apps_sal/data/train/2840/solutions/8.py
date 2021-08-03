def withdraw(n):
    fifties = 1 if n % 20 else 0
    twenties = int(n / 20) - 2 if fifties else int(n / 20)
    hundreds = int(20 * twenties / 100)
    twenties = twenties - hundreds * 5
    return [hundreds, fifties, twenties]
