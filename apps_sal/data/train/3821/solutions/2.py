def chinese_zodiac(year):
    animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    diff = year-1984
    animalIndex = diff%12
    eleIndex = diff//2
    eleIndex = eleIndex%5
    return "{} {}".format(elements[eleIndex], animals[animalIndex])
