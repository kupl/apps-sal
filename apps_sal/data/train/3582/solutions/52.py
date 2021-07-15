import re
def is_digit(n):
    print(n)
    return True if re.findall("\A[\d]\Z",n) != [] else False
