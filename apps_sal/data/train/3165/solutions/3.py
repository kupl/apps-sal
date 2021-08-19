import requests
r = requests.get('https://oeis.org/A139250/b139250.txt').text.splitlines()


def toothpick(n):
    return int(r[n].split()[1])
