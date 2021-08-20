def rot13(message):
    abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split() * 2
    abc_upper = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split() * 2
    res = ''
    for i in message:
        if i in abc_upper:
            res += abc_upper[abc_upper.index(i) + 13]
        elif i in abc:
            res += abc[abc.index(i) + 13]
        else:
            res += i
    return res
