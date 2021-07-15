def word_square(letters):
    if (len(letters))**.5 != int((len(letters))**.5):
        return False
    else:
        n = int((len(letters))**.5)
    s = set(letters)
    one, two = 0,0
    for letter in s:
        if letters.count(letter) == 1: one += 1
        if letters.count(letter) == 2: two += 1
    return one <= n and two <= n**2-n        
