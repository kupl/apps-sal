t = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}


def numbers_of_letters(n):
    x = [''.join([t[i] for i in str(n)])]
    while int(n) != len(x[-1]):
        n = len(x[-1])
        x.append(''.join([t[i] for i in str(n)]))
    return x
