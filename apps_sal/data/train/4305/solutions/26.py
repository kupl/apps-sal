def order_weight(strng):
    return ' '.join(sorted(sorted(filter(lambda x: not not x, strng.split(' '))),key=lambda x:sum(map(int,x))))
