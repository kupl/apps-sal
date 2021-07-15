def order_weight(string):
    valueList = [sum([int(char) for char in num]) for num in string.split()]
    return ' '.join([tup[1] for tup in sorted(zip(valueList,string.split()))])
