import requests

r = requests.get('https://oeis.org/A014575/b014575.txt')

vampire_numbers = [int(d.split(' ')[1]) for d in r.text.strip().split('\n')]


def VampireNumber(n):
    return vampire_numbers[n - 1]
