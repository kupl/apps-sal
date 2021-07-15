def chinese_zodiac(year):
    s = ''
    a = ['Rat','Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    e = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    
    e1 = (year - 1984) // 2 % 5 
    a1 = (year - 1984) % 12
       
    s = e[e1] + ' ' + a[a1]
    return s
