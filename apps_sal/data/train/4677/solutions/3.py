from itertools import product
from string import digits
from hashlib import md5

crack = {md5(pin.encode()).hexdigest(): pin for pin in map(''.join, product(digits, repeat=5))}.get
