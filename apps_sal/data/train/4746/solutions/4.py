from functools import reduce
fisHex=lambda s:reduce(lambda x,y: x^y,[int(i,16) for i in s if i in "ABCDEFabcdef"] or [0])
