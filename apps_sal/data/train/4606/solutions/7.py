ones = [''] + 'I II III IV V VI VII VIII IX'.split()
tens = [''] + 'X XX XXX XL L LX LXX LXXX XC'.split()
hundreds = [''] + 'C CC CCC CD D DC DCC DCCC CM'.split()
thousands = [''] + 'M MM MMM MMMM'.split()
good = ['MMMMM'] + [i + j + k + l for i in thousands for j in hundreds for k in tens for l in ones]


def valid_romans(arr):
    return [i for i in arr if i and i in good]
