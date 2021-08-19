def valid_card(card):
    card_str = card.replace(' ', '')
    index = 0
    sum_card = 0
    while index < len(card_str):
        number = 0
        if index % 2 == 0:
            number = int(card_str[index]) * 2
        else:
            number = int(card_str[index])
        if number >= 10:
            number_arr = list(str(number))
            number = 0
            for num in number_arr:
                number += int(num)
        sum_card += number
        index += 1
    return sum_card % 10 == 0
