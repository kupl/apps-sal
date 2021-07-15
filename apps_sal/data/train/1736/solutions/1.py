import re
def is_sequential(string):
    return string in "1234567890" or string in "9876543210"

def is_interesting(number, awesome_phrases):
    print (number)
    interestingness = 2
    for i in (number, number + 1, number + 2):
        if (number != i):
            interestingness = 1
        if (i < 100):
            continue
        if (i in awesome_phrases):
            return interestingness
        i = str(i)
        if re.match(r"^\d0+$", i):
            return interestingness
        if i == i[::-1]:
            return interestingness
        if is_sequential(i):
            return interestingness
        if re.match(r"^(\d)\1+$", i):
            return interestingness
    
    
    return 0
