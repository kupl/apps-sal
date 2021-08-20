def square_it(n):
    return len(str(n)) ** 0.5 % 1 and 'Not a perfect square!' or '\n'.join(map(''.join, zip(*[iter(str(n))] * int(len(str(n)) ** 0.5))))
