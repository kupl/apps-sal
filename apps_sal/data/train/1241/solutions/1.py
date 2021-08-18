def winner_is(x: int, n: int, stones: [int]) -> str:
    odd_piles = sum([j % 2 for j in stones])
    if x % 2 == 1:
        if x // 2 >= odd_piles or (n % 2 == 1 and x // 2 >= n - odd_piles):
            return "Jesse"
        return "Walter"
    elif x // 2 >= n - odd_piles and n % 2 == 1:
        return "Walter"
    return "Jesse"


def driver():
    pile = []
    for i in range(int(input())):
        n, x = map(int, input().split())
        stones = list(map(int, input().split()))
        pile.append(winner_is(x, n, stones))
    print(*pile, sep="\n")


driver()
