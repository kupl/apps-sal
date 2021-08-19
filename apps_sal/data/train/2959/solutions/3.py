def optimal_number_of_coins(n, coins):
    dicto = {}

    def optimal_number_of_coinss(n, coins, mino=0, indo=0):
        key = f'{n}indo:{indo}mino:{mino}'
        if key in dicto:
            return dicto[key]
        if not n:
            return mino
        if indo >= len(coins):
            return 10000
        if n < 0:
            return 100100
        dicto[key] = min(optimal_number_of_coinss(n - coins[indo], coins, mino + 1, indo), optimal_number_of_coinss(n, coins, mino, indo + 1))
        return dicto[key]
    return optimal_number_of_coinss(n, coins)
