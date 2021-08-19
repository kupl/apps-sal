def valid_card(card):
    li = []
    print(card)
    digits = card.replace(' ', '')[::-1]
    for (i, d) in enumerate(digits):
        di = int(d)
        if i % 2 != 0:
            di = di * 2
            if di > 9:
                di = di - 9
            li.append(di)
        else:
            li.append(di)
    return True if sum(li) % 10 == 0 else False
