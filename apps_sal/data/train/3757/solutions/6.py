import math
def round_to_five(numbers):
    output = []
    for n in numbers:
        if n % 5 == 0:
            output.append(int(n))
        elif (n % 10 < 5 and n % 5 < 2.5) or (n % 10 > 5 and n % 5 >= 2.5):
            output.append(int(round(n,-1)))
        elif (n % 10 < 5 and n % 5 >= 2.5):
            output.append(int(round(n,-1) + 5))
        else:
            output.append(int(round(n,-1) - 5))
    return output

