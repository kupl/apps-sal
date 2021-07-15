from itertools import count
def disarium_number(number):
    return ('Not !!', 'Disarium !!')[number == sum(map(pow, map(int, str(number)), count(1)))]
