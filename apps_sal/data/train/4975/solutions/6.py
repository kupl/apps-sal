def solution(n):
    return ' M MM MMM'.split(' ')[n // 1000] + ' C CC CCC CD D DC DCC DCCC CM'.split(' ')[n // 100 % 10] + ' X XX XXX XL L LX LXX LXXX XC'.split(' ')[n // 10 % 10] + ' I II III IV V VI VII VIII IX'.split(' ')[n % 10]
