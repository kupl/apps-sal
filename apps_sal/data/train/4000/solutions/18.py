def strong_num(number):
    return ('Not Strong !!', 'STRONG!!!!')[number == sum([[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][int(x)]
                                                          for x in str(number)])]
