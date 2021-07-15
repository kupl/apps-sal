def house_of_cards(floors):
    if floors <= 0:
        raise ValueError('The input must be an integer greater than 0')
    return 2 + sum(3*i + 2 for i in range(1,floors+1))
