def order_weight(strng): return ' '.join([x for _, x in sorted(zip([sum([int(j) for j in i]) for i in strng.split(' ')], strng.split(' ')))])
