guess_my_number = lambda g, n='123-451-2345': ''.join((('#' + c)[c in '-' + g] for c in n))
