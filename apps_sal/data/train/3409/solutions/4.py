def fish(shoal):
    fishes = sorted(shoal)
    my_size = 1
    amount_for_next_size = 4

    for i in range(len(fishes)):
        if int(fishes[i]) > my_size:
            break
        amount_for_next_size -= int(fishes[i])
        if amount_for_next_size <= 0:
            my_size += 1
            amount_for_next_size += my_size * 4
    return my_size
