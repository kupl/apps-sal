guess_my_number = lambda guess, number='123-451-2345': ''.join([x if x in guess or x == '-' else '#' for x in list(number)])
