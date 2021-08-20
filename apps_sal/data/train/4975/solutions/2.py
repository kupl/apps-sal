units = ' I II III IV V VI VII VIII IX'.split(' ')
tens = ' X XX XXX XL L LX LXX LXXX XC'.split(' ')
hundreds = ' C CC CCC CD D DC DCC DCCC CM'.split(' ')
thousands = ' M MM MMM'.split(' ')


def solution(n):
    return thousands[n // 1000] + hundreds[n % 1000 // 100] + tens[n % 100 // 10] + units[n % 10]
