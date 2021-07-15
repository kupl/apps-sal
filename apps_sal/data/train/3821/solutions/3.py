def chinese_zodiac(year):
    EPOCH = 1924
    ANIMALS = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    ELEMENTS = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    year -= EPOCH
    res = ELEMENTS[(year // 2) % len(ELEMENTS)], ANIMALS[year % len(ANIMALS)]
    return " ".join(res)
