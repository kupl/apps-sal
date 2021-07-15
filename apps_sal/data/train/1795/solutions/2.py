# https://en.wikipedia.org/wiki/Eight_queens_puzzle#Existence_of_solutions
def nQueen(n):
    if n <= 3:
        return [[], [0], [], []][n]
    odds = list(range(1, n+1, 2))
    evens = list(range(2, n+1, 2))
    if n % 6 == 2:
        p1, p3 = odds.index(1), odds.index(3)
        odds[p1], odds[p3] = odds[p3], odds[p1]
        odds.remove(5)
        odds.append(5)
    elif n % 6 == 3:
        evens.remove(2)
        evens.append(2)
        odds.remove(1)
        odds.remove(3)
        odds.extend([1, 3])
    return [n - a for a in evens + odds]
