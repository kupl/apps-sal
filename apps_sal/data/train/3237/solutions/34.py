def even_or_odd(number):
    number = str(number)
    even = ['0', '2', '4', '6', '8']
    if number[-1] in even:
            return "Even"
    else:
        return "Odd"
