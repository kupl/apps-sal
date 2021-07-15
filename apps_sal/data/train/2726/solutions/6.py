def square_it(digits):
    d = len(str(digits))**.5
    return '\n'.join(map(''.join, zip(*[iter(str(digits))]*int(d)))) if int(d) == d  else 'Not a perfect square!'
