def tiy_fizz_buzz(string):
    new_string = ''
    for i in string:
        if i.isupper():
            new_string += 'Iron'
            if i in ('AEIOU'):
                new_string += ' Yard'
        elif i in ('aeiou'):
            new_string += 'Yard'
        else:
            new_string += i
    return new_string
