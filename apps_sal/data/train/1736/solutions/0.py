def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0
