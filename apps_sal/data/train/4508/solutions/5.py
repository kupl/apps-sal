import requests


def VampireNumber(n):
    r = requests.get('https://oeis.org/A014575/b014575.txt').text.splitlines()

    return int(r[n - 1].split()[1])
