from collections import defaultdict
def men_still_standing(cards):
    book = [defaultdict(int), defaultdict(int)]
    f = lambda book: sum((-1 for b in book.values() if b > 1), 11)
    cnt = [11, 11]
    for c in cards:
        team, num, card = c[0] == 'B', c[1:-1], c[-1]
        book[team][num] += (1,2)[card == 'R']
        cnt = list(map(f, book))
        if min(cnt) < 7:
            break
    return tuple(cnt)
