from itertools import islice

def f(tbl=str.maketrans('01', '10')):
    x = '0'
    while True:
        yield from x[len(x)//2:]
        x += x.translate(tbl)
        
def thue_morse(n):
    return ''.join(islice(f(), n))
