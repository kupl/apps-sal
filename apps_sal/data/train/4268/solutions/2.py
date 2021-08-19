import requests
from bisect import bisect
MAGIC = [int(x) for x in requests.get('https://oeis.org/b144688.txt').text.split()[1::2]]


def next_num(n):
    return MAGIC[bisect(MAGIC, n)] if n < MAGIC[-1] else None
