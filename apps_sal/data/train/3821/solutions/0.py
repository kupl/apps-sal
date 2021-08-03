animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']


def chinese_zodiac(year):
    year -= 1984
    return elements[year // 2 % 5] + " " + animals[year % 12]
