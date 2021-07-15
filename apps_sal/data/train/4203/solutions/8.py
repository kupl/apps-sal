def caffeineBuzz(n):
    coffe = 'mocha_missing!'
    if n%3 == 0:
        coffe = 'Coffee' if n%4==0 else 'Java'
        coffe = coffe + ('Script' if n%2==0 else '')
    return coffe
