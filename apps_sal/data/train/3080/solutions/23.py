from collections import OrderedDict 
who_is_paying = lambda n: list(OrderedDict.fromkeys([n,n[0:2:]]))
