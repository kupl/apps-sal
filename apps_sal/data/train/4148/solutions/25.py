
def sum_digits(number):
    sum = 0
    number = abs(number)
    number = str(number)
    for i in number:
        print(i)
        sum += int(i)
    return sum
        

