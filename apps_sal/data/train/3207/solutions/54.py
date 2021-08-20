def reverseWords(s):
    car = s.split()
    car = car[::-1]
    return ' '.join(car)
